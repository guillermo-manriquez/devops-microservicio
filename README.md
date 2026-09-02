## Estrategia de Ramificación (GitFlow)

Para este proyecto elegimos utilizar **GitFlow** porque nos permite mantener un historial limpio y separar estrictamente el entorno de desarrollo continuo de las versiones estables de producción.

*   **Vs. Trunk-Based Development:** Trunk-Based requiere un alto nivel de madurez en pruebas automatizadas y despliegues para integrar todo directamente a la rama principal. Dado el alcance colaborativo de este microservicio, preferimos la seguridad de trabajar en ramas aisladas (`develop` y `feature/`) antes de impactar el código principal.
*   **Vs. GitHub Flow:** Aunque GitHub Flow es más simple (todo nace y vuelve a `main`), GitFlow nos otorga el control de usar ramas `hotfix/` para inyectar parches de emergencia directamente a producción, sin arrastrar código inestable que aún esté en fase de desarrollo.

## CI/CD y Entorno Cloud Simulado

La Integración Continua (CI) se configuró mediante **GitHub Actions**. Este pipeline se dispara automáticamente en dos eventos clave:
1.  Cada vez que se hace un `push` a la rama `develop`.
2.  Al abrir un `Pull Request` hacia la rama `main`.

**Entorno Cloud Simulado:** GitHub Actions cumple el rol de nuestro entorno cloud simulado. Las pruebas de `pytest` no corren localmente en nuestras máquinas, sino que se ejecutan en servidores virtuales efímeros (runners de Ubuntu) alojados en la nube de GitHub, validando la integridad del código de forma remota e independiente.

## Convenciones y Flujo de Trabajo

*   **Convenciones de Commits:** Utilizamos *Conventional Commits* para mantener la semántica.
    *   `feat:` para nuevas características.
    *   `fix:` para solución de errores.
    *   `docs:` para cambios en la documentación.
*   **Nomenclatura de Ramas:** Todas las ramas deben seguir el formato `feature/<descripcion>`, `hotfix/<descripcion>` o `docs/<descripcion>`.
*   **Estrategias de Revisión:** La integración de código se realiza estrictamente a través de Pull Requests. Ningún integrante aprueba su propio código; se requiere la revisión y aprobación (Approve) explícita del otro desarrollador antes de ejecutar el merge.

## Estructura de Carpetas

*   `app/`: Lógica principal del microservicio.
    *   `main.py`: Endpoints y configuración de la API (FastAPI).
    *   `models.py`: Modelos de datos (Pydantic).
*   `tests/`: Pruebas automatizadas.
    *   `test_main.py`: Tests de integración y unitarios.
*   `.github/workflows/`: Archivos YAML de configuración para GitHub Actions.