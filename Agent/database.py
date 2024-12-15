import json
import os
# database.json example
# {
#    已选择的课程
#    "courses": [
#     {
#       "name": "软件安全",
#       "attribute": "选修"
#     }......]
#    所有课程，作为模拟课程数据库
#    "all_courses": [
#     {
#       "name": "软件安全",
#       "attribute": "选修"
#     },
#     {
#       "name": "C++",
#       "attribute": "必修"
#     }......]
# }

#
class Database:
    """
    处理数据库增删改查的类
    """
    def __init__(self):
        if os.path.exists('./database.json'):
            with open('./database.json', 'r', encoding="utf-8") as f:
                self.db = json.load(f)
        else:
            self.db = {}
            with open('./database.json', 'w', encoding="utf-8") as f:
                json.dump(self.db, f)

    # Save the database to the file
    def save(self):
        with open('./database.json', 'w', encoding="utf-8") as f:
            json.dump(self.db, f, ensure_ascii=False)

    # Add a course to the selected courses
    # name must exist in all_courses
    def add_course(self, name):
        for c in self.db['all_courses']:
            if name == c['name']:
                for course in self.db['courses']:
                    if course['name'] == name:
                        return "Course already selected"
                self.db['courses'].append({'name': name, 'attribute': c['attribute']})
                self.save()
                return "Course added"

        return "Course not found"

    def show_selected_courses(self):
        print("Courses selected:")
        for c in self.db['courses']:
            print(c['name'], c['attribute'])

    def show_all_courses(self):
        print("All courses:")
        for c in self.db['all_courses']:
            print(c['name'], '(', c['attribute'], ')')

    # Show selected courses with the specific attribute(必修or选修)
    def show_selected_conditional_courses(self, attribute):
        for c in self.db['courses']:
            if c['attribute'] == attribute:
                print(c['name'])

    # Show all courses with the specific attribute(必修or选修)
    def show_all_conditional_courses(self, attribute):
        for c in self.db['all_courses']:
            if c['attribute'] == attribute:
                print(c['name'])

    def get_selected_courses(self):
        if (self.db['courses'] == []):
            return "No courses selected"
        return self.db['courses']

    # Get selected courses with the specific attribute(必修or选修)
    def get_selected_conditional_courses(self, attribute):
        return [course for course in self.db['courses'] if course['attribute'] == attribute]

    # Get all courses with the specific attribute(必修or选修)
    def get_all_conditional_courses(self, attribute):
        return [course for course in self.db['all_courses'] if course['attribute'] == attribute]

    # True on finding the specific course and removed it, False otherwise
    def remove_course(self, name) -> bool:
        for course in self.db['courses']:
            if course['name'] == name:
                self.db['courses'].remove(course)
                self.save()
                return True
        return False
