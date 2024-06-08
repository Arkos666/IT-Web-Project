from wagtail.models import Page
from wagtail.fields import RichTextField

class HomePage(Page):
    # Añade campos para la página de inicio
    pass

class ServicesPage(Page):
    # Añade campos para la página de servicios
    pass

class BlogIndexPage(Page):
    # Añade campos para el índice del blog
    pass

class BlogPage(Page):
    body = RichTextField()
    # Otros campos para una entrada de blog

class ContactPage(Page):
    # campos para ContactPage
    pass
