class CourseService:
    def __init__(self, db):
        self.collection = db.get_collection('courses')

    def get_all_courses(self):
        return list(self.collection.find({}))

    def create_course(self, course):
        result = self.collection.insert_one(course)
        return {"id": str(result.inserted_id)}
