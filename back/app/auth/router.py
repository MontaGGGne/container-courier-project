from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi_mail import FastMail, MessageSchema
from jinja2 import Environment, FileSystemLoader

from app.auth.auth import create_access_token
from app.auth.dao import AuthDAO
from app.auth.dependencies import get_current_user
from app.auth.schemas import CCode, CLogin, CMCode
from app.auth.utils import generate_code
from app.config import conf
from app.models import Users
from app.users.dao import UsersDAO

router = APIRouter(prefix="/auth", tags=["Авторизация"])

template_loader = FileSystemLoader(searchpath="app/templates")
template_env = Environment(loader=template_loader)
template_file = "email.html"


@router.post("/createcode")
async def send_test(data: CMCode):
    email_to = data.email
    user_id = await UsersDAO.find_by_email(data.email)
    if user_id:
        user_id = user_id.id
        code = generate_code()
        template = template_env.get_template(template_file)
        html_content = template.render(email=email_to, code=code)
        message = MessageSchema(
            subject=f"Ваш код подтверждения: {code}",
            recipients=[email_to],
            body=html_content,
            subtype="html",
        )
        fm = FastMail(conf)
        await fm.send_message(message)
        obj = CCode(id=user_id, code=str(code))
        await AuthDAO.update(obj)
        return "ok"
    else:
        raise HTTPException(status_code=400)


@router.post("/login")
async def login(response: Response, login_data: CLogin):
    user = await AuthDAO.find_one_or_none(email=login_data.email)
    if not user:
        raise HTTPException(500)
    if user:
        if login_data.code == user.code:
            access_token = create_access_token({"sub": str(user.email)})
            response.headers["Authorization"] = f"{access_token}"
            response.set_cookie("access_token", access_token, httponly=True)
            return {"access_token": access_token}
        else:
            raise HTTPException(400)


@router.post("/verify-token")
async def verify_token(user: Users = Depends(get_current_user)):
    result = {"valid": False, "staff": False}
    if user:
        result["valid"] = True
        result["staff"] = user.if_staff
    return result


@router.post("/logout")
async def logout(response: Response):
    response.delete_cookie("access_token")
