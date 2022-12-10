# Hay una base de datos que se puede remixear. Me imagino tres modalidades con distintos pesos para cada caso

import markovify

# Get raw text as string.
with open("/home/emi/proyectos/tres/latex/sec/introduccion.tex") as f:
    text_a = f.read()
with open("/home/emi/proyectos/tres/latex/sec/antecedentes.tex") as g:
    text_b = g.read()
# with open("/home/emi/proyectos/tfjs-models/face-landmarks-detection/anti/txt/txtsc3.txt") as h:
#    text_c = h.read()
#with open("/home/emi/proyectos/tfjs-models/face-landmarks-detection/anti/txt/index.txt") as j:
#    text_d = j.read()
# with open("/home/emi/proyectos/tfjs-models/face-landmarks-detection/anti/txt/indexTHREEBCN.txt") as k:
  #  text_e = k.read()


# Build the model.
#text_model = markovify.Text(text)

model_txt1 = markovify.Text(text_a, well_formed = False, state_size=2)
model_txt2 = markovify.Text(text_b, well_formed = False, state_size=2)
#model_txt3 = markovify.Text(text_c, well_formed = False, state_size=2)
#model_txt4 = markovify.Text(text_d, well_formed = False, state_size=2)
#model_txt5 = markovify.Text(text_e, well_formed = False, state_size=2)
#model_combo = markovify.combine([ model_txt5, model_txt2, model_txt3, model_txt4, model_txt1 ], [ 1, 1, 1, 1, 1 ])
model_combo = markovify.combine([ model_txt2, model_txt1 ], [ 1, 1 ])


# Print five randomly-generated sentences
#for i in range(10):
#    print(model_combo.make_sentence())

# Print three randomly-generated sentences of no more than 280 characters
for i in range(100):
    print(model_combo.make_short_sentence(50))

# with open("Output.txt", "w") as text_file:
#    for i in range(100): 
#        text_file.write(model_combo.make_short_sentence(150))   
