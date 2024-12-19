CREATE TABLE todo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    taskdesc VARCHAR(255) NOT NULL,
    is_completed BOOLEAN DEFAULT FALSE,
    Urgencyrank INT DEFAULT 0,                   
    assigned_to VARCHAR(100) NULL,            
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    deadline_date TIMESTAMP NULL,
    Remarks TEXT NULL                           
);