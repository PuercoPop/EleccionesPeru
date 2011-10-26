/* Función que retira espacios en blanco al principio y al final de la cadena*/
/* Reemplaza además dos o mas espacios por uno solo dentro de la cadena.*/

function trim(inputString){
    if (typeof inputString != "string") 
        return inputString;

    var retValue = inputString;
    var ch = retValue.substring(0, 1);
    while (ch == " ") 
    { // Espacios al comienzo
        retValue = retValue.substring(1, retValue.length);
        ch = retValue.substring(0, 1);
    }

    ch = retValue.substring(retValue.length-1, retValue.length);
    while (ch == " ") 
    { // Espacios al final
        retValue = retValue.substring(0, retValue.length-1);
        ch = retValue.substring(retValue.length-1, retValue.length);
    }

    while (retValue.indexOf("  ") != -1) 
    { // Dos espacios
        retValue = retValue.substring(0, retValue.indexOf("  ")) + retValue.substring(retValue.indexOf("  ")+1, retValue.length); // Again, there are two spaces in each of the strings
    }
    return retValue; 
}

function fechahoy(){
    var diasemana = new Array('Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado');
    var nombremes = new Array('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'setiembre', 'octubre', 'noviembre', 'diciembre');
    var ahora;
    var fecha = new Date();
    var anio = fecha.getYear();
    if(anio<1000)
        anio += 1900;
    var mes = fecha.getMonth();
    var dia = fecha.getDay();
    var num = fecha.getDate();
    if(num<=9) num='0'+num;
    ahora = diasemana[dia] + " " + num + " de " + nombremes[mes] + " de " + anio;
    return ahora;
} 

function fechacortahoy(){
    var ahora;
    var fecha = new Date();
    var anio = fecha.getYear();
    var mes = fecha.getMonth()+1;
    var dia = fecha.getDay();
    var num = fecha.getDate();
    if(num<=9) num='0'+num;
    if(mes<=9) mes='0'+mes;
    if(anio<1000) anio += 1900;
    ahora = num + "/" + mes + "/" + anio
    return ahora;
}

function hora_actual(){
    var ahora;
    var hora = new Date();
    var hh = hora.getHours();
    var mm = hora.getMinutes();
    var ss = hora.getSeconds();
    if(hh<=9) hh='0'+hh;
    if(mm<=9) mm='0'+mm;
    if(ss<=9) ss='0'+ss;
    ahora = hh + ":" + mm + ":" + ss
    return ahora;
}

function cadena_valida(myfield,e,cadena){
	switch(cadena){
		//CARACTERES VALIDOS	
		case 1: cadena1="ABCDEFGHIJKLMNOPQRSTUVWYXZ0123456789abcdefghijklmnopqrstuvwxyz\/?#$%&()=*+}{[]_-> <:,.;ñÑáéíóúÁÉÍÓÚº";break;
		//CARACTERES SOLO TEXTO SIN NUMEROS
		case 2: cadena1="ABCDEFGHIJKLMNOPQRSTUVWYXZabcdefghijklmnopqrstuvwxyz,.;ñÑáéíóúÁÉÍÓÚ ";break;
		//NUMEROS ENTEROS SIN DECIMALES
		case 3: cadena1="0123456789";break;
		//NUMEROS DECIMALES
		case 4: cadena1="0123456789.";break;
		//CARACTERES PARA CORREO ELECTRONICO
		case 5: cadena1="ABCDEFGHIJKLMNOPQRSTUVWYXZ0123456789abcdefghijklmnopqrstuvwxyz._-@ ";break;
		//TELEFONO
		case 6: cadena1="0123456789 -";break;
		//CARACTERES DE USUARIO Y CONTRASEÑA VALIDOS
		case 7: cadena1="ABCDEFGHIJKLMNOPQRSTUVWYXZ0123456789abcdefghijklmnopqrstuvwxyz";break;
	}
	
	var key;
	var keychar;
	var keycadena=cadena1;
	if (window.event)
		key = window.event.keyCode;
	else if (e)
		key = e.which;
	else
		return true;
	keychar = String.fromCharCode(key);
	
	if ((key==null) || (key==0) || (key==8) || (key==9) || (key==13) || (key==27) )
		return true;
	else 
		if (((keycadena).indexOf(keychar) > -1))
	return true;
	
	return false;
}
