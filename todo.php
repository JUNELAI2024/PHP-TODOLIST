<?php

$taskdesc = '';
$urgencyRank = 0;
$assignedTo = '';
$deadlineDate = null;
$remarks = '';
$readyToStore = false;

function connectToDB() {
    $conn = new mysqli("localhost", "root", "", "your_database_name"); // Update with your database name
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    return $conn;
}

$conn = connectToDB();

if ($_SERVER['REQUEST_METHOD'] === "POST" && isset($_POST['submit'])) {
    $taskdesc = htmlspecialchars(trim($_POST['taskdesc']));
    $urgencyRank = (int)$_POST['urgencyrank'];
    $assignedTo = htmlspecialchars(trim($_POST['assigned_to']));
    $deadlineDate = htmlspecialchars(trim($_POST['deadline_date']));
    $remarks = htmlspecialchars(trim($_POST['remarks']));

    // Validate input
    if (!empty($taskdesc)) {
        $readyToStore = true;
    }
}

if ($readyToStore && $conn) {
    $stmt = $conn->prepare("INSERT INTO todo (taskdesc, Urgencyrank, assigned_to, deadline_date, Remarks) VALUES (?, ?, ?, ?, ?)");
    $stmt->bind_param("sisss", $taskdesc, $urgencyRank, $assignedTo, $deadlineDate, $remarks);
    
    if ($stmt->execute()) {
        echo "<p>Task added successfully!</p>";
    } else {
        echo "<p>Error: " . $stmt->error . "</p>";
    }
    $stmt->close();
}

if ($conn) {
    $sql = "SELECT * FROM todo ORDER BY created_date DESC";
    $result = $conn->query($sql);
    $tasks = "";

    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            $tasks .= '<div class="entry">
                <div class="entry-header">
                    <span class="entry-name">' . htmlspecialchars($row['taskdesc']) . '</span>
                    <span class="entry-date">' . date('d M Y', strtotime($row['created_date'])) . '</span>
                </div>
                <p>Assigned to: ' . htmlspecialchars($row['assigned_to']) . '</p>
                <p>Urgency: ' . (int)$row['Urgencyrank'] . '</p>
                <p>Deadline: ' . ($row['deadline_date'] ? date('d M Y', strtotime($row['deadline_date'])) : 'No deadline') . '</p>
                <p>Remarks: ' . htmlspecialchars($row['Remarks']) . '</p>
                <p>Status: ' . ($row['is_completed'] ? 'Completed' : 'Pending') . '</p>
            </div>';
        }
    } else {
        $tasks = "<p>No tasks available.</p>";
    }
}

$conn->close();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Todo List</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            background: linear-gradient(to bottom, #f0f0f0, #d9d9d9);
            color: #333;
            font-family: Arial, sans-serif;
            padding: 20px;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
        }

        .form-container {
            background: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }

        .entry {
            background: #fff;
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 15px;
            margin-bottom: 10px;
        }

        .entry-header {
            display: flex;
            justify-content: space-between;
            margin-bottom: 10px;
        }

        .entry-name {
            font-weight: bold;
        }

        .entry-date {
            color: #999;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="form-container">
            <h2>Add a New Task</h2>
            <form method="post">
                <label for="taskdesc">Task Description:</label>
                <input type="text" name="taskdesc" required>
                
                <label for="urgencyrank">Urgency Rank (0-10):</label>
                <input type="number" name="urgencyrank" min="0" max="10" value="0">
                
                <label for="assigned_to">Assigned To:</label>
                <input type="text" name="assigned_to">
                
                <label for="deadline_date">Deadline Date:</label>
                <input type="date" name="deadline_date">
                
                <label for="remarks">Remarks:</label>
                <textarea name="remarks"></textarea>
                
                <button name="submit" type="submit">Add Task</button>
            </form>
        </div>

        <h2>Current Tasks</h2>
        <div class="tasks-container">
            <?= $tasks ?>
        </div>
    </div>
</body>
</html>