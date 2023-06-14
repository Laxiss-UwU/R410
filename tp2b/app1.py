from fastapi import FastAPI
app = FastAPI()

donnees = {
    'lieux': [
        'Paris',
        'Lyon',
        'Marseille',
        'Montpellier',
        'Toulon',
        'Lilles',
        'Nantes',
	'Rouen']
}

@app.get ("/lieux")
async def get_lieux():
    return {'donnees': donnees}

@app.post("/lieux")
async def post_lieu(lieu: str):
    if lieu in donnees['lieux']:
        return {'donnees': donnees, 'message': "Le lieu est déja référencé !"}
    else:
        donnees['lieux'].append(lieu)
        return {'donnees': donnees, 'message': "Le lieu a correctement été ajouté."}

@app.delete("/lieux")
async def delete_lieu(lieu: str):
    if lieu in donnees['lieux']:
        donnees['lieux'].remove(lieu)
        return {'donnees': donnees, 'message':'Le lieu a correctement été supprimé.'}
    else:
        return {'donnees': donnees, 'message': "Le lieu n'est pas référencé !"}