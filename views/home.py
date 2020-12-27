import fastapi
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from services import report_service

router = fastapi.APIRouter()
templates = Jinja2Templates('templates')


@router.get('/')
async def index(request: Request):
    events = await report_service.get_reports()
    data = {'request': request, 'events': events}

    return templates.TemplateResponse('home/index.html', data)


@router.get('/favicon.ico')
def favicon():
    return fastapi.responses.RedirectResponse(url='/static/img/favicon.ico')
