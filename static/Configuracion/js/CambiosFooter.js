function CambioLetraFooter() {
    $(document).ready(function() {
        let TipoLetra = document.querySelector("#TipoLetra2").value;
        let body = document.querySelectorAll(".tipo2");
        body.forEach(texto => {
            if (texto.style.fontFamily = TipoLetra) {
                texto.style.fontFamily = TipoLetra
                texto = texto.style.fontFamily = TipoLetra
                console.log(texto)
            }
        });
    })
}
function ColorLetraFooter(event) {
    const codigo = event.which || event.keyCode;
    if(codigo === 13){
        $(document).ready(function(){
            let ColorLetra = document.querySelector("#ColorLetra2").value;
            let texto = document.querySelectorAll(".tipo2");
            texto.forEach(textos =>{
                if (textos.style.color = ColorLetra) {
                    textos.style.color = ColorLetra
                    textos = textos.style.color = ColorLetra 
                }
            });
            
        });
    }  
}



function ColorFondoFooter(event) {
    const codigo = event.which || event.keyCode;
    if(codigo === 13){
        let ColorFondo = document.getElementById("ColorFondo2").value;
        let body = document.getElementById("texto2");
        body.style.backgroundColor = ColorFondo;
    }
    
}

function CambiarTamanoFooter(event) {
    const codigo = event.which || event.keyCode;
    if(codigo === 13){
        $(document).ready(function(){
            let TamanoLetra = document.querySelector("#TamanoLetra2").value;
            let tamano = document.querySelectorAll("#text3");
            tamano.forEach(tamanos =>{
                if (tamanos.style.fontSize = TamanoLetra) {
                    tamanos.style.fontSize = TamanoLetra+("px")
                    tamanos = tamanos.style.fontSize = TamanoLetra+("px") 
                }
            });
            
        });
    }  
}
function CambiarTamano2Footer(event) {
    const codigo = event.which || event.keyCode;
    if(codigo === 13){
        $(document).ready(function(){
            let TamanoLetra2 = document.querySelector("#TamanoLetra2").value;
            let tamano2 = document.querySelectorAll("#text4");
            tamano2.forEach(tamanos2 =>{
                if (tamanos2.style.fontSize = TamanoLetra2) {
                    tamanos2.style.fontSize = TamanoLetra2+("px")
                    tamanos2 = tamanos2.style.fontSize = TamanoLetra2+("px") 
                }
            });
            
        });
    }  
}
