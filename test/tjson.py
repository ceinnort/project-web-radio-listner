import pickle

radios = {
    "radio france": {
        "france inter" : {
            "url" : "url direct" ,
            "logo" : "url logo" ,
            "info direct" : "des infos sur le direct, si possibe qui se mettent a jours et recolter sur leur site" ,
            "couleur" : "la couleur, si possible recolter depuis le CSS" ,
            "programme" : "info possible sur le programme"
        },
        "france info" : {
            "url" : "url direct" ,
            "logo" : "url logo" ,
            "info direct" : "des infos sur le direct, si possibe qui se mettent a jours et recolter sur leur site" ,
            "couleur" : "la couleur, si possible recolter depuis le CSS" ,
            "programme" : "info possible sur le programme"
        },
        "france culture" : {
            "url" : "url direct" ,
            "logo" : "url logo" ,
            "info direct" : "des infos sur le direct, si possibe qui se mettent a jours et recolter sur leur site" ,
            "couleur" : "la couleur, si possible recolter depuis le CSS" ,
            "programme" : "info possible sur le programme"
        },
        "france musique" : {
            "url" : "url direct" ,
            "logo" : "url logo" ,
            "info direct" : "des infos sur le direct, si possibe qui se mettent a jours et recolter sur leur site" ,
            "couleur" : "la couleur, si possible recolter depuis le CSS" ,
            "programme" : "info possible sur le programme"
        }
    },
    "groupe RTL" : {
        "RTL" : {
            "url" : "url direct" ,
            "logo" : "url logo" ,
            "info direct" : "des infos sur le direct, si possibe qui se mettent a jours et recolter sur leur site" ,
            "couleur" : "la couleur, si possible recolter depuis le CSS" ,
            "programme" : "info possible sur le programme"
        },
        "RTL 2" : {
            "url" : "url direct" ,
            "logo" : "url logo" ,
            "info direct" : "des infos sur le direct, si possibe qui se mettent a jours et recolter sur leur site" ,
            "couleur" : "la couleur, si possible recolter depuis le CSS" ,
            "programme" : "info possible sur le programme"
        },
        "fun radio" : {
            "url" : "url direct" ,
            "logo" : "url logo" ,
            "info direct" : "des infos sur le direct, si possibe qui se mettent a jours et recolter sur leur site" ,
            "couleur" : "la couleur, si possible recolter depuis le CSS" ,
            "programme" : "info possible sur le programme"
        }
    }
}

def dict2file(dict, file):
    pickle.dump(dict, open(file, "wb"))

def file2dict(file):
    return pickle.load(open(file, "rb"))

dict2file(radios, "infoRadios")
