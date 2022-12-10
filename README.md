# Tres Estudios Abiertos

La bitácora se ha trasladado a otro lado 

Prácticas performáticas, audiovisuales y experimentales con lenguajes de programación como instancias de conocimiento.

## Compilación pdf 

Compilar el documento, actualizar bibliografía 

1.- clonar
> git clone https://github.com/emilioocelotl/tres.git

2.- scripts
> source automation

3.- compilar doc principal
> tres

## Compilación web

> make4ht -x tres.tex

## Para juntar páginas

pdfjam tres.pdf --nup 2x1 --suffix 2up --landscape --trim '0mm 0mm 0mm 0mm' --papersize '{297mm,460mm}' --outfile temp.pdff

## Recursos

- [latex-css](https://github.com/vincentdoerig/latex-css)

## Cambios

- La bitácora se ha trasladado a otro lado
- Cambios estructurales sugeridos por tutores de acuerdo a la pertinencia de la reflexión y no de las piezas 

## Pendientes

- [ ] Bajo la lógica de la reestructuración ya no es posible escribir artículos académicos para cada pieza y que a su vez sean capítulos. Entonces podrían realizarse artículos por objetivo funcional e incluso por "nivel" descrito. 
- [ ] ¿ Escribir en markdown y luego compilar a latex ? El problema de las citas
- [ ] Reordenar lo ya escrito 
- [ ] Investigación y práctica exahustiva con librerías y lenguajes que coinciden con el proyecto 
- [ ] Decisiones de estructura
- [ ] PDF u otra forma de compartir el documento para la lectura 
- [ ] Eliminar archivos en carpetas como anti ( con automat ) 
- [ ] Compilar web tipo documento
- [ ] Web tipo otra cosa
