from .DBConnection import DBConnection

class StudentInfoTable:
    def insert_a_student(self, name, subjects_scores):
        """Insert a student and their subjects with scores."""
        with DBConnection() as connection:
            cursor = connection.cursor()
            connection.commit()

            for subject, score in subjects_scores.items():
                cursor.execute("INSERT INTO subject_info (name, subject, score) VALUES (?, ?, ?);",
                               (name, subject, score))
            connection.commit()

    def delete_a_student(self, name):
        """Delete a student and their associated subject records."""
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM subject_info WHERE name=?;", (name,))
            connection.commit()

    def update_a_student(self, name, subjects_scores):
        """Update a student's name and their subject scores."""
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM subject_info WHERE name=?;", (name,))
            for subject, score in subjects_scores.items():
                cursor.execute("INSERT INTO subject_info (name, subject, score) VALUES (?, ?, ?);",
                               (name, subject, score))
            connection.commit()

    def select_all_students(self):
        command = "SELECT * FROM subject_info"
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            records = cursor.fetchall()
        return records
