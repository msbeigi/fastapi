from fastapi import FastAPI, HTTPException, status
import uvicorn
from api import main as m


app_main=FastAPI()


@app_main.get("/hello/")
def hello_world():
	return m.hello_world()

@app_main.get("/getcourses/")
def get_courses_():
      return m.get_courses()

@app_main.get("/getcourses/{level}/")
def get_courses(level: str):
      return m.get_courses(level)

@app_main.delete("/delcourses/{course_id}/", status_code=status.HTTP_204_NO_CONTENT)
def delete_course(course_id:int):
      return m.delete_course(course_id)

@app_main.post("/makecourses/")
def create_course(new_course:m.Course):
      return m.create_course(new_course=new_course)


@app_main.put("/editcourses/")
def update_course(course_id:int,course:m.Course):
    return m.update_course(course_id,course)


if __name__ == '__main__':
    uvicorn.run(app_main,port=8001,host='0.0.0.0')

