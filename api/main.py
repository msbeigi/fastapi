from fastapi import FastAPI, HTTPException, status
from typing import Union,Optional
from pydantic import BaseModel

class Course(BaseModel):
	title:str
	teacher:str
	students:str
	level:str

courses={
	1:{
		"title":"Modern History",
		"teacher":"Ms. Doe",
		"students":["Harry","Frodo"],
		"level":"advanced"
	},
	2:{
		"title":"Modern tech",
		"teacher":"Mrs. Hisingle",
		"students":["Franchesta"],
		"level":"Intermediate"
	}
}
app=FastAPI()

@app.get("/api/hello/")
def hello_world():
	return {"message":"Hello world"}


@app.get("/api/courses/")
def get_courses():
	return courses

@app.get("/api/courses/{level}/")
def get_courses(level: Union[str, None]=None):
	leve_courses = []
	if level:
		for index in courses.keys():
			if courses[index]["level"]==level:
				leve_courses.append(courses[index])
	return leve_courses

@app.get("/api/courses/{course_id}/")
def get_course(course_id:int):
	try:
		return courses[course_id]
	except KeyError:
		raise HTTPException(status_code=404,detail=f"{course_id} not in the range")

@app.delete("/api/courses/{course_id}/", status_code=status.HTTP_204_NO_CONTENT)
def delete_course(course_id:int):
	try:
		del courses[course_id]
	except KeyError:
		raise HTTPException(status_code=404,detail=f"{course_id} not in the range")


@app.post("/api/courses/")
def create_course(new_course:Course):
	course_id=max(courses.keys())+1
	courses[course_id]=new_course.model_dump()
	return courses

@app.put("/api/courses/")
def update_course(course_id:int,course:Course):
	try:
		course_=courses[course_id]
		course_["title"]=course.title
		course_["students"]=course.students
		course_["teacher"]=course.teacher
		course_["level"]=course.level
		# courses[course_id]=course_
		return course_
	except KeyError:
		raise HTTPException(status_code=404,detail=f"{course_id} not in the range")

