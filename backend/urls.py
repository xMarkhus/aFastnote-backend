from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


# Função para redirecionar a raiz para o Swagger
def redirect_to_docs(request):
    return redirect('/swagger/')


urlpatterns = [
    path("admin/", admin.site.urls),

    # Rota raiz redirecionando para o Swagger
    path('', redirect_to_docs),  # Redireciona a raiz para o Swagger

    # Esquema da API
    path('schema/', SpectacularAPIView.as_view(), name='schema'),

    # UI do Swagger
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # UI do Redoc
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # Minhas rotas
    path("api/v1/", include("authentication.urls")),
    path("api/v1/", include("user.urls")),
    path("api/v1/", include("api.urls")),
]
