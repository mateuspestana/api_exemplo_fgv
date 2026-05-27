from fastapi import FastAPI
import pandas as pd

app = FastAPI(title="API Dados")

df_alunos = pd.read_excel("dados.xlsx", sheet_name="Alunos")
df_professores = pd.read_excel("dados.xlsx", sheet_name="Professores")
df_cursos = pd.read_excel("dados.xlsx", sheet_name="Cursos")


@app.get("/")
def root():
    return {"endpoints": ["/alunos", "/professores", "/cursos"]}


@app.get("/alunos")
def get_alunos():
    return df_alunos.to_dict(orient="records")


@app.get("/professores")
def get_professores():
    return df_professores.to_dict(orient="records")


@app.get("/cursos")
def get_cursos():
    return df_cursos.to_dict(orient="records")

@app.post("/sobenome")
def post_sobenome(sobenome: str):
    return {"nome em caixa alta": sobenome.upper()}

@app.post("/descenome")
def post_descenome(descenome: str):
    return {"nome em caixa baixa": descenome.lower()}

@app.get('/alunos/{nome}/notas')
def get_notas(nome: str):
    aluno = df_alunos[df_alunos['nome'] == nome]
    if aluno.empty:
        return {"error": "Aluno não encontrado"}
    notas = aluno[['nota']].to_dict(orient='records')[0]
    return {"notas": notas}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
