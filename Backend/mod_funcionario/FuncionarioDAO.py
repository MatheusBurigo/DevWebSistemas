from fastapi import APIRouter

router = APIRouter()

# Criar as rotas/endpoints: GET, POST, PUT, DELETE
@router.get("/funcionario/", tags=["Funcionário"])
def get_funcionario():
    return {"msg": "get todos executado"}, 200

@router.get("/funcionario/{id}", tags=["Funcionário"])
def get_funcionario(id: int):
    return {"msg": "get um executado"}, 200

@router.post("/funcionario/", tags=["Funcionário"])
def post_funcionario():
    return {"msg": "post executado"}, 200

@router.put("/funcionario/{id}", tags=["Funcionário"])
def put_funcionario(id: int):
    return {"msg": "put executado"}, 20