# Coffea — Landing page (HTML + CSS)

TP4 · Diseño UX-UI · Landing estática para la cafetería ficticia **Coffea**. Solo HTML5 semántico y CSS3 (sin JavaScript, frameworks ni preprocesadores).

## Estructura

```
coffea/
├── index.html
├── 404.html
├── netlify.toml
├── convertir-imagenes.py   # ayuda para generar AVIF/WebP/JPG
├── css/
│   ├── main.css            # @layer + @import de las capas
│   ├── tokens.css          # custom properties (colores, tipos, espacios, medidas)
│   ├── base.css            # reset, tipografía base, :focus-visible
│   ├── layout.css          # contenedor, franjas, títulos de sección
│   ├── utilities.css       # .visually-hidden, .skip-link, prefers-reduced-motion
│   └── components/         # header, hero, categories, product-card, carousel,
│                           # promo, testimonial-card, newsletter, footer, not-found
└── assets/
    ├── img/
    └── icons/
```

## Convenciones

- BEM estricto: `.bloque`, `.bloque__elemento`, `.bloque--modificador`.
- Capas: `@layer tokens, base, layout, components, utilities;` (sin `!important`, salvo en `prefers-reduced-motion`).
- Sin valores sueltos: colores, fuentes, radios, espacios y medidas salen de `tokens.css`.
- Mobile-first: estilos base desde 360 px y `min-width` en 768, 1024 y 1440 px.

## Correr en local

Abrir la carpeta en VS Code y usar la extensión **Live Server** sobre `index.html`. No requiere build.

## Imágenes

Las imágenes incluidas son provisorias. Para reemplazarlas: poner las fotos en `originales/` con los nombres indicados en `convertir-imagenes.py` y ejecutar `python convertir-imagenes.py` (requiere `pip install pillow`). Confirmar la licencia de las fotos antes de publicar.

## Despliegue en Netlify

1. Subir el proyecto a un repositorio de GitHub o GitLab.
2. En Netlify: *Add new site → Import an existing project* y elegir el repositorio.
3. Build command: vacío. Publish directory: `.`
4. Cada push a `main` publica a producción y cada Pull Request genera un Deploy Preview.

`css/` y `assets/` se sirven con caché `immutable`: si cambiás un archivo ya publicado, renombralo con versión (por ejemplo `main.v2.css`) y actualizá la referencia.
