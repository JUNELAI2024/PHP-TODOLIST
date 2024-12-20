CREATE TABLE todo (
    id INT AUTO_INCREMENT PRIMARY KEY,          
    taskdesc VARCHAR(255) NOT NULL,             
    is_completed BOOLEAN NOT NULL DEFAULT FALSE, 
    Urgencyrank INT NOT NULL DEFAULT 0,          
    assigned_to VARCHAR(100) NOT NULL,           
    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,  
    deadline_date TIMESTAMP NULL,               
    Remarks TEXT NULL                             
);