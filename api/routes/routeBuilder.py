
from . import db, request
from ..utils.decoratorSQLAlchemyErrorHandler import baseSQLAlchemyErrorHandler

def makeBaseRoutes(BaseModel, bp):
            
    @bp.route("/getAll", methods=["GET"], endpoint='getAll')
    @baseSQLAlchemyErrorHandler       
    def getAll():
            models = db.session.execute(db.select(BaseModel).order_by(BaseModel.id)).scalars()
            return [model.as_dict() for model in models]

    @bp.route("/post", methods=["POST"], endpoint='post')
    @baseSQLAlchemyErrorHandler
    def post():
        model = BaseModel(**request.json)
        db.session.add(model)
        db.session.commit()

        return {"message":"model criado"}


    @bp.route("/get/<int:id>",  methods=["GET"], endpoint='get')
    @baseSQLAlchemyErrorHandler
    def get(id):

        model = db.get_or_404(BaseModel, id)
        if model:
            return model.as_dict()
        
        else:
            return {"message":"model nao encontrado"} 
   
    @bp.route("/put/<int:id>", methods=["PUT"], endpoint='put')
    @baseSQLAlchemyErrorHandler
    def put(id):
        model = BaseModel.query.get(id)
        if model:
            update_from_json(request.json,model)
            db.session.commit()
            return model.as_dict()
        
        else:
            return {"message":"model nao encontrado"}  
        
    
    @bp.route("/delete/<int:id>", methods=["DELETE"], endpoint='delete')
    @baseSQLAlchemyErrorHandler
    def delete(id):
        
        model = db.get_or_404(BaseModel, id)
        
        if model:
            db.session.delete(model)
            db.session.commit()
            return {"message":"deletado"}   

        else:
            return {"message":"model nao encontrado"}  
    
    def update_from_json(dados, obj):
        for chave, valor in dados.items():
            if getattr(obj, chave):
                setattr(obj, chave, valor)
    
