from dependency_injector import containers, providers


class Container(containers.DeclarativeContainer):
    """IoC container of the application core components."""
    config = providers.Configuration()
