from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()
APP_KEY = "UDHFTGHVCJUDI"

class arrrg(BaseModel):
    fruit: str
    color: str
    goodness: str
    what: bool = False

class uuurg(BaseModel):
    name: str
    Grades: int
    gender: str


fruits = [
   arrrg(fruit="apple", color="red", goodness="yes"),
    arrrg(fruit="orange", color="orange", goodness="yes"),
    arrrg(fruit="Grapes", color="purple", goodness="no"),
    arrrg(fruit="cherry", color="red red", goodness="yes"),
    arrrg(fruit="Bananas", color="yellow", goodness="no"),
    arrrg(fruit="Fish", color="its not a fruit", goodness="meh"),
    arrrg(fruit="man", color="i dont encourage cannibalism", goodness="yes"),
    arrrg(fruit="kiwi", color="green", goodness="no"),
    arrrg(fruit="Mango", color="light yellow", goodness="yes"),
    arrrg(fruit="Pomegranate", color="dark purple", goodness="yes"),
    arrrg(fruit="watermelon", color="green with stripes", goodness="no"),
    arrrg(fruit="pineapple", color="some kind of yellow", goodness="yes"),
    arrrg(fruit="Lemon", color="very very yellow", goodness="yes"),
    arrrg(fruit="Strawberry", color="red with dots", goodness="yes"),
    arrrg(fruit="Avocado", color="green but not green completely", goodness="yes"),
    arrrg(fruit="I can't think of any", color="bro cant think of any fruits", goodness="what"),
    arrrg(fruit="coke", color="thats a drink", goodness="yes"),
    arrrg(fruit="fanta", color="thats soda", goodness="yes"),
    arrrg(fruit="water", color="bruh we just degrading" ,goodness="yes"),
    arrrg(fruit="nothing", color="it has no color", goodness="nothing")
]

Grades = [
    uuurg(name="leon", Grades=9, gender="male"),
    uuurg(name="Richard", Grades=8, gender="male"),
     uuurg(name="God", Grades=69, gender="he got none")
]


@router.post("/student_data")
async def add_new_grades(grades: uuurg):
    Grades.append(grades)
    return {"msg": "grades added"}

@router.post("fruits_data")
async def add_new_fruits(fruit: arrrg):
    fruits.append(fruit)
    return {"msg": "fruits added"}

@router.get("/fruits/get_info")
async def get_fruits(fruit: arrrg, appid: str):
    if appid != APP_KEY:
        return {"msg": "Key is incorrect"}
    for fruits_info in fruits:
        if fruit.lower() == fruits_info['fruit'].lower():
            return fruits_info
    return {"msg": "fruit not found"}


@router.get("/grades/get_info")
async def get_grades(grade: uuurg, appid: str):
    if appid != APP_KEY:
        return {"msg": "Key is incorrect"}
    for grades_info in Grades:
        if grade.lower() == grades_info['name'].lower():
            return grades_info
    return {"msg": "grade not found"}
