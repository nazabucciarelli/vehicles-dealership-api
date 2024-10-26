from vehicles.repositories.category_repository import CategoryRepository

def add_request_path(request):
    return {
        'current_path': request.path
    }

def add_categories_to_context(request):
    category_repository = CategoryRepository()
    categories = category_repository.get_all()
    return {
        'categories': categories
    }