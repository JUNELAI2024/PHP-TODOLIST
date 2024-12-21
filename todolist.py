
import tkinter as tk
from tkinter import messagebox
import mysql.connector

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        # Connect to MySQL database
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",  # Your MySQL username
                password="junelai2024",  # Your MySQL password
                database="todo_db"
            )
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
            self.root.quit()  # Close the application if the connection fails

        # Create UI elements
        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.pack(pady=10)
        self.task_entry.insert(0, "Task Description")

        self.urgency_entry = tk.Entry(self.root, width=40)
        self.urgency_entry.pack(pady=10)
        self.urgency_entry.insert(0, "Urgency Rank (0-10)")

        self.assigned_to_entry = tk.Entry(self.root, width=40)
        self.assigned_to_entry.pack(pady=10)
        self.assigned_to_entry.insert(0, "Assigned To")

        self.deadline_entry = tk.Entry(self.root, width=40)
        self.deadline_entry.pack(pady=10)
        self.deadline_entry.insert(0, "Deadline (YYYY-MM-DD HH:MM:SS)")

        self.remarks_entry = tk.Entry(self.root, width=40)
        self.remarks_entry.pack(pady=10)
        self.remarks_entry.insert(0, "Remarks")

        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=10)

        self.task_listbox = tk.Listbox(self.root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        self.delete_task_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(pady=10)

        self.load_tasks()

    def load_tasks(self):
        """Load tasks from the database into the listbox."""
        self.task_listbox.delete(0, tk.END)  # Clear the listbox
        self.cursor.execute("SELECT taskdesc FROM todo")
        for (taskdesc,) in self.cursor.fetchall():
            self.task_listbox.insert(tk.END, taskdesc)

    def add_task(self):
        taskdesc = self.task_entry.get()
        urgencyrank = self.urgency_entry.get()
        assigned_to = self.assigned_to_entry.get()
        deadline_date = self.deadline_entry.get()
        remarks = self.remarks_entry.get()

        if taskdesc and urgencyrank and assigned_to:
            try:
                self.cursor.execute(
                    "INSERT INTO todo (taskdesc, Urgencyrank, assigned_to, deadline_date, Remarks) VALUES (%s, %s, %s, %s, %s)",
                    (taskdesc, urgencyrank, assigned_to, deadline_date, remarks)
                )
                self.conn.commit()
                self.load_tasks()  # Refresh the listbox
                # Clear input fields
                self.task_entry.delete(0, tk.END)
                self.urgency_entry.delete(0, tk.END)
                self.assigned_to_entry.delete(0, tk.END)
                self.deadline_entry.delete(0, tk.END)
                self.remarks_entry.delete(0, tk.END)
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")
        else:
            messagebox.showwarning("Warning", "Please fill in all required fields.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            selected_task = self.task_listbox.get(selected_task_index)

            # Delete from the database
            self.cursor.execute("DELETE FROM todo WHERE taskdesc = %s", (selected_task,))
            self.conn.commit()

            self.load_tasks()  # Refresh the listbox
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def __del__(self):
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()