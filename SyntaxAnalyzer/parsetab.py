
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programaleftANDORleftSUMARESTAleftMULTIPLICACIONDIVISIONrightNOTleftASIGNACIONleftPUNTO_COMAnonassocMAYOR_QUEMENOR_QUEMAYOR_IGUALMENOR_IGUALIGUAL_IGUALDIFERENTEAND ASIGNACION COMA CON_PASO DESDE DIFERENTE DIVISION ENTONCES FIN FIN_MIENTRAS FIN_PARA FIN_SI HACER HASTA HASTA_QUE IDENTIFICADOR IGUAL_IGUAL INICIO LITERAL_BOOLEANO LITERAL_CADENA LITERAL_DECIMAL LITERAL_ENTERO MAYOR_IGUAL MAYOR_QUE MENOR_IGUAL MENOR_QUE MIENTRAS MOSTRAR MULTIPLICACION NOT OR PARA PARENTESIS_DER PARENTESIS_IZQ PUNTO_COMA REPETIR RESTA SI SINO SUMA TIPOprograma : INICIO declaraciones FINdeclaraciones : declaraciones declaracion_simple\n| declaraciones declaracion_con_asignacion\n| declaraciones constante\n| declaraciones asignacion\n| declaraciones sentencia_if\n| declaraciones sentencia_mientras\n| declaraciones sentencia_para\n| declaraciones sentencia_repetir\n| declaraciones sentencia_mostrar\n| emptyempty :sentencia_if : SI PARENTESIS_IZQ expresion PARENTESIS_DER ENTONCES declaraciones FIN_SI\n| SI PARENTESIS_IZQ expresion PARENTESIS_DER ENTONCES declaraciones SINO declaraciones FIN_SIsentencia_mientras : MIENTRAS PARENTESIS_IZQ expresion PARENTESIS_DER HACER declaraciones FIN_MIENTRASsentencia_para : PARA IDENTIFICADOR DESDE expresion HASTA expresion HACER declaraciones FIN_PARA\n| PARA IDENTIFICADOR DESDE expresion HASTA expresion CON_PASO expresion HACER declaraciones FIN_PARAsentencia_repetir : REPETIR declaraciones HASTA_QUE PARENTESIS_IZQ expresion PARENTESIS_DER PUNTO_COMAsentencia_mostrar : MOSTRAR lista_expresiones PUNTO_COMAexpresion : LITERAL_ENTERO\n| LITERAL_DECIMAL\n| LITERAL_CADENA\n| LITERAL_BOOLEANO\n| IDENTIFICADOR\n| expresion SUMA expresion\n| expresion RESTA expresion\n| expresion MULTIPLICACION expresion\n| expresion DIVISION expresion\n| expresion AND expresion\n| expresion OR expresion\n| NOT expresion\n| expresion MAYOR_QUE expresion\n| expresion MENOR_QUE expresion\n| expresion MAYOR_IGUAL expresion\n| expresion MENOR_IGUAL expresion\n| expresion IGUAL_IGUAL expresion\n| expresion DIFERENTE expresion\n| PARENTESIS_IZQ expresion PARENTESIS_DERlista_expresiones : lista_expresiones COMA expresion\n| expresiondeclaracion_simple : TIPO IDENTIFICADOR PUNTO_COMAdeclaracion_con_asignacion : TIPO IDENTIFICADOR ASIGNACION expresion PUNTO_COMAasignacion : IDENTIFICADOR ASIGNACION expresion PUNTO_COMAconstante : TIPO IDENTIFICADOR ASIGNACION expresion'
    
_lr_action_items = {'INICIO':([0,],[2,]),'$end':([1,5,],[0,-1,]),'FIN':([2,3,4,6,7,8,9,10,11,12,13,14,30,31,32,33,34,37,44,58,60,61,67,68,69,70,71,72,73,74,75,76,77,78,79,80,89,91,94,98,99,102,],[-12,5,-11,-2,-3,-4,-5,-6,-7,-8,-9,-10,-20,-21,-22,-23,-24,-41,-19,-31,-44,-43,-25,-26,-27,-28,-29,-30,-32,-33,-34,-35,-36,-37,-38,-42,-13,-15,-18,-14,-16,-17,]),'TIPO':([2,3,4,6,7,8,9,10,11,12,13,14,20,27,30,31,32,33,34,37,44,58,60,61,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,85,86,89,90,91,92,94,95,96,98,99,100,101,102,],[-12,15,-11,-2,-3,-4,-5,-6,-7,-8,-9,-10,-12,15,-20,-21,-22,-23,-24,-41,-19,-31,-44,-43,-25,-26,-27,-28,-29,-30,-32,-33,-34,-35,-36,-37,-38,-42,-12,-12,15,15,-13,-12,-15,-12,-18,15,15,-14,-16,-12,15,-17,]),'IDENTIFICADOR':([2,3,4,6,7,8,9,10,11,12,13,14,15,19,20,21,23,24,25,27,30,31,32,33,34,35,36,37,38,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,60,61,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,85,86,89,90,91,92,93,94,95,96,98,99,100,101,102,],[-12,16,-11,-2,-3,-4,-5,-6,-7,-8,-9,-10,22,26,-12,34,34,34,34,16,-20,-21,-22,-23,-24,34,34,-41,34,34,-19,34,34,34,34,34,34,34,34,34,34,34,34,34,-31,-44,-43,34,-25,-26,-27,-28,-29,-30,-32,-33,-34,-35,-36,-37,-38,-42,-12,-12,34,16,16,-13,-12,-15,-12,34,-18,16,16,-14,-16,-12,16,-17,]),'SI':([2,3,4,6,7,8,9,10,11,12,13,14,20,27,30,31,32,33,34,37,44,58,60,61,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,85,86,89,90,91,92,94,95,96,98,99,100,101,102,],[-12,17,-11,-2,-3,-4,-5,-6,-7,-8,-9,-10,-12,17,-20,-21,-22,-23,-24,-41,-19,-31,-44,-43,-25,-26,-27,-28,-29,-30,-32,-33,-34,-35,-36,-37,-38,-42,-12,-12,17,17,-13,-12,-15,-12,-18,17,17,-14,-16,-12,17,-17,]),'MIENTRAS':([2,3,4,6,7,8,9,10,11,12,13,14,20,27,30,31,32,33,34,37,44,58,60,61,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,85,86,89,90,91,92,94,95,96,98,99,100,101,102,],[-12,18,-11,-2,-3,-4,-5,-6,-7,-8,-9,-10,-12,18,-20,-21,-22,-23,-24,-41,-19,-31,-44,-43,-25,-26,-27,-28,-29,-30,-32,-33,-34,-35,-36,-37,-38,-42,-12,-12,18,18,-13,-12,-15,-12,-18,18,18,-14,-16,-12,18,-17,]),'PARA':([2,3,4,6,7,8,9,10,11,12,13,14,20,27,30,31,32,33,34,37,44,58,60,61,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,85,86,89,90,91,92,94,95,96,98,99,100,101,102,],[-12,19,-11,-2,-3,-4,-5,-6,-7,-8,-9,-10,-12,19,-20,-21,-22,-23,-24,-41,-19,-31,-44,-43,-25,-26,-27,-28,-29,-30,-32,-33,-34,-35,-36,-37,-38,-42,-12,-12,19,19,-13,-12,-15,-12,-18,19,19,-14,-16,-12,19,-17,]),'REPETIR':([2,3,4,6,7,8,9,10,11,12,13,14,20,27,30,31,32,33,34,37,44,58,60,61,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,85,86,89,90,91,92,94,95,96,98,99,100,101,102,],[-12,20,-11,-2,-3,-4,-5,-6,-7,-8,-9,-10,-12,20,-20,-21,-22,-23,-24,-41,-19,-31,-44,-43,-25,-26,-27,-28,-29,-30,-32,-33,-34,-35,-36,-37,-38,-42,-12,-12,20,20,-13,-12,-15,-12,-18,20,20,-14,-16,-12,20,-17,]),'MOSTRAR':([2,3,4,6,7,8,9,10,11,12,13,14,20,27,30,31,32,33,34,37,44,58,60,61,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,85,86,89,90,91,92,94,95,96,98,99,100,101,102,],[-12,21,-11,-2,-3,-4,-5,-6,-7,-8,-9,-10,-12,21,-20,-21,-22,-23,-24,-41,-19,-31,-44,-43,-25,-26,-27,-28,-29,-30,-32,-33,-34,-35,-36,-37,-38,-42,-12,-12,21,21,-13,-12,-15,-12,-18,21,21,-14,-16,-12,21,-17,]),'HASTA_QUE':([4,6,7,8,9,10,11,12,13,14,20,27,30,31,32,33,34,37,44,58,60,61,67,68,69,70,71,72,73,74,75,76,77,78,79,80,89,91,94,98,99,102,],[-11,-2,-3,-4,-5,-6,-7,-8,-9,-10,-12,43,-20,-21,-22,-23,-24,-41,-19,-31,-44,-43,-25,-26,-27,-28,-29,-30,-32,-33,-34,-35,-36,-37,-38,-42,-13,-15,-18,-14,-16,-17,]),'FIN_SI':([4,6,7,8,9,10,11,12,13,14,30,31,32,33,34,37,44,58,60,61,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,85,89,90,91,94,95,98,99,102,],[-11,-2,-3,-4,-5,-6,-7,-8,-9,-10,-20,-21,-22,-23,-24,-41,-19,-31,-44,-43,-25,-26,-27,-28,-29,-30,-32,-33,-34,-35,-36,-37,-38,-42,-12,89,-13,-12,-15,-18,98,-14,-16,-17,]),'SINO':([4,6,7,8,9,10,11,12,13,14,30,31,32,33,34,37,44,58,60,61,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,85,89,91,94,98,99,102,],[-11,-2,-3,-4,-5,-6,-7,-8,-9,-10,-20,-21,-22,-23,-24,-41,-19,-31,-44,-43,-25,-26,-27,-28,-29,-30,-32,-33,-34,-35,-36,-37,-38,-42,-12,90,-13,-15,-18,-14,-16,-17,]),'FIN_MIENTRAS':([4,6,7,8,9,10,11,12,13,14,30,31,32,33,34,37,44,58,60,61,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,86,89,91,94,98,99,102,],[-11,-2,-3,-4,-5,-6,-7,-8,-9,-10,-20,-21,-22,-23,-24,-41,-19,-31,-44,-43,-25,-26,-27,-28,-29,-30,-32,-33,-34,-35,-36,-37,-38,-42,-12,91,-13,-15,-18,-14,-16,-17,]),'FIN_PARA':([4,6,7,8,9,10,11,12,13,14,30,31,32,33,34,37,44,58,60,61,67,68,69,70,71,72,73,74,75,76,77,78,79,80,89,91,92,94,96,98,99,100,101,102,],[-11,-2,-3,-4,-5,-6,-7,-8,-9,-10,-20,-21,-22,-23,-24,-41,-19,-31,-44,-43,-25,-26,-27,-28,-29,-30,-32,-33,-34,-35,-36,-37,-38,-42,-13,-15,-12,-18,99,-14,-16,-12,102,-17,]),'ASIGNACION':([16,22,],[23,38,]),'PARENTESIS_IZQ':([17,18,21,23,24,25,35,36,38,42,43,45,46,47,48,49,50,51,52,53,54,55,56,57,65,83,93,],[24,25,36,36,36,36,36,36,36,36,65,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'LITERAL_ENTERO':([21,23,24,25,35,36,38,42,45,46,47,48,49,50,51,52,53,54,55,56,57,65,83,93,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'LITERAL_DECIMAL':([21,23,24,25,35,36,38,42,45,46,47,48,49,50,51,52,53,54,55,56,57,65,83,93,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'LITERAL_CADENA':([21,23,24,25,35,36,38,42,45,46,47,48,49,50,51,52,53,54,55,56,57,65,83,93,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'LITERAL_BOOLEANO':([21,23,24,25,35,36,38,42,45,46,47,48,49,50,51,52,53,54,55,56,57,65,83,93,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'NOT':([21,23,24,25,35,36,38,42,45,46,47,48,49,50,51,52,53,54,55,56,57,65,83,93,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'PUNTO_COMA':([22,28,29,30,31,32,33,34,39,58,60,66,67,68,69,70,71,72,73,74,75,76,77,78,79,88,],[37,44,-40,-20,-21,-22,-23,-24,61,-31,80,-39,-25,-26,-27,-28,-29,-30,-32,-33,-34,-35,-36,-37,-38,94,]),'DESDE':([26,],[42,]),'COMA':([28,29,30,31,32,33,34,58,66,67,68,69,70,71,72,73,74,75,76,77,78,79,],[45,-40,-20,-21,-22,-23,-24,-31,-39,-25,-26,-27,-28,-29,-30,-32,-33,-34,-35,-36,-37,-38,]),'SUMA':([29,30,31,32,33,34,39,40,41,58,59,60,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,84,87,97,],[46,-20,-21,-22,-23,-24,46,46,46,-31,46,46,46,46,-25,-26,-27,-28,46,46,-32,-33,-34,-35,-36,-37,-38,46,46,46,]),'RESTA':([29,30,31,32,33,34,39,40,41,58,59,60,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,84,87,97,],[47,-20,-21,-22,-23,-24,47,47,47,-31,47,47,47,47,-25,-26,-27,-28,47,47,-32,-33,-34,-35,-36,-37,-38,47,47,47,]),'MULTIPLICACION':([29,30,31,32,33,34,39,40,41,58,59,60,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,84,87,97,],[48,-20,-21,-22,-23,-24,48,48,48,-31,48,48,48,48,48,48,-27,-28,48,48,-32,-33,-34,-35,-36,-37,-38,48,48,48,]),'DIVISION':([29,30,31,32,33,34,39,40,41,58,59,60,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,84,87,97,],[49,-20,-21,-22,-23,-24,49,49,49,-31,49,49,49,49,49,49,-27,-28,49,49,-32,-33,-34,-35,-36,-37,-38,49,49,49,]),'AND':([29,30,31,32,33,34,39,40,41,58,59,60,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,84,87,97,],[50,-20,-21,-22,-23,-24,50,50,50,-31,50,50,50,50,-25,-26,-27,-28,-29,-30,-32,-33,-34,-35,-36,-37,-38,50,50,50,]),'OR':([29,30,31,32,33,34,39,40,41,58,59,60,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,84,87,97,],[51,-20,-21,-22,-23,-24,51,51,51,-31,51,51,51,51,-25,-26,-27,-28,-29,-30,-32,-33,-34,-35,-36,-37,-38,51,51,51,]),'MAYOR_QUE':([29,30,31,32,33,34,39,40,41,58,59,60,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,84,87,97,],[52,-20,-21,-22,-23,-24,52,52,52,52,52,52,52,52,52,52,52,52,52,52,None,None,None,None,None,None,-38,52,52,52,]),'MENOR_QUE':([29,30,31,32,33,34,39,40,41,58,59,60,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,84,87,97,],[53,-20,-21,-22,-23,-24,53,53,53,53,53,53,53,53,53,53,53,53,53,53,None,None,None,None,None,None,-38,53,53,53,]),'MAYOR_IGUAL':([29,30,31,32,33,34,39,40,41,58,59,60,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,84,87,97,],[54,-20,-21,-22,-23,-24,54,54,54,54,54,54,54,54,54,54,54,54,54,54,None,None,None,None,None,None,-38,54,54,54,]),'MENOR_IGUAL':([29,30,31,32,33,34,39,40,41,58,59,60,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,84,87,97,],[55,-20,-21,-22,-23,-24,55,55,55,55,55,55,55,55,55,55,55,55,55,55,None,None,None,None,None,None,-38,55,55,55,]),'IGUAL_IGUAL':([29,30,31,32,33,34,39,40,41,58,59,60,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,84,87,97,],[56,-20,-21,-22,-23,-24,56,56,56,56,56,56,56,56,56,56,56,56,56,56,None,None,None,None,None,None,-38,56,56,56,]),'DIFERENTE':([29,30,31,32,33,34,39,40,41,58,59,60,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,84,87,97,],[57,-20,-21,-22,-23,-24,57,57,57,57,57,57,57,57,57,57,57,57,57,57,None,None,None,None,None,None,-38,57,57,57,]),'PARENTESIS_DER':([30,31,32,33,34,40,41,58,59,67,68,69,70,71,72,73,74,75,76,77,78,79,84,],[-20,-21,-22,-23,-24,62,63,-31,79,-25,-26,-27,-28,-29,-30,-32,-33,-34,-35,-36,-37,-38,88,]),'HASTA':([30,31,32,33,34,58,64,67,68,69,70,71,72,73,74,75,76,77,78,79,],[-20,-21,-22,-23,-24,-31,83,-25,-26,-27,-28,-29,-30,-32,-33,-34,-35,-36,-37,-38,]),'HACER':([30,31,32,33,34,58,63,67,68,69,70,71,72,73,74,75,76,77,78,79,87,97,],[-20,-21,-22,-23,-24,-31,82,-25,-26,-27,-28,-29,-30,-32,-33,-34,-35,-36,-37,-38,92,100,]),'CON_PASO':([30,31,32,33,34,58,67,68,69,70,71,72,73,74,75,76,77,78,79,87,],[-20,-21,-22,-23,-24,-31,-25,-26,-27,-28,-29,-30,-32,-33,-34,-35,-36,-37,-38,93,]),'ENTONCES':([62,],[81,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'declaraciones':([2,20,81,82,90,92,100,],[3,27,85,86,95,96,101,]),'empty':([2,20,81,82,90,92,100,],[4,4,4,4,4,4,4,]),'declaracion_simple':([3,27,85,86,95,96,101,],[6,6,6,6,6,6,6,]),'declaracion_con_asignacion':([3,27,85,86,95,96,101,],[7,7,7,7,7,7,7,]),'constante':([3,27,85,86,95,96,101,],[8,8,8,8,8,8,8,]),'asignacion':([3,27,85,86,95,96,101,],[9,9,9,9,9,9,9,]),'sentencia_if':([3,27,85,86,95,96,101,],[10,10,10,10,10,10,10,]),'sentencia_mientras':([3,27,85,86,95,96,101,],[11,11,11,11,11,11,11,]),'sentencia_para':([3,27,85,86,95,96,101,],[12,12,12,12,12,12,12,]),'sentencia_repetir':([3,27,85,86,95,96,101,],[13,13,13,13,13,13,13,]),'sentencia_mostrar':([3,27,85,86,95,96,101,],[14,14,14,14,14,14,14,]),'lista_expresiones':([21,],[28,]),'expresion':([21,23,24,25,35,36,38,42,45,46,47,48,49,50,51,52,53,54,55,56,57,65,83,93,],[29,39,40,41,58,59,60,64,66,67,68,69,70,71,72,73,74,75,76,77,78,84,87,97,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> INICIO declaraciones FIN','programa',3,'p_programa','Parser.py',27),
  ('declaraciones -> declaraciones declaracion_simple','declaraciones',2,'p_declaraciones','Parser.py',36),
  ('declaraciones -> declaraciones declaracion_con_asignacion','declaraciones',2,'p_declaraciones','Parser.py',37),
  ('declaraciones -> declaraciones constante','declaraciones',2,'p_declaraciones','Parser.py',38),
  ('declaraciones -> declaraciones asignacion','declaraciones',2,'p_declaraciones','Parser.py',39),
  ('declaraciones -> declaraciones sentencia_if','declaraciones',2,'p_declaraciones','Parser.py',40),
  ('declaraciones -> declaraciones sentencia_mientras','declaraciones',2,'p_declaraciones','Parser.py',41),
  ('declaraciones -> declaraciones sentencia_para','declaraciones',2,'p_declaraciones','Parser.py',42),
  ('declaraciones -> declaraciones sentencia_repetir','declaraciones',2,'p_declaraciones','Parser.py',43),
  ('declaraciones -> declaraciones sentencia_mostrar','declaraciones',2,'p_declaraciones','Parser.py',44),
  ('declaraciones -> empty','declaraciones',1,'p_declaraciones','Parser.py',45),
  ('empty -> <empty>','empty',0,'p_empty','Parser.py',53),
  ('sentencia_if -> SI PARENTESIS_IZQ expresion PARENTESIS_DER ENTONCES declaraciones FIN_SI','sentencia_if',7,'p_sentencia_if','Parser.py',64),
  ('sentencia_if -> SI PARENTESIS_IZQ expresion PARENTESIS_DER ENTONCES declaraciones SINO declaraciones FIN_SI','sentencia_if',9,'p_sentencia_if','Parser.py',65),
  ('sentencia_mientras -> MIENTRAS PARENTESIS_IZQ expresion PARENTESIS_DER HACER declaraciones FIN_MIENTRAS','sentencia_mientras',7,'p_sentencia_mientras','Parser.py',78),
  ('sentencia_para -> PARA IDENTIFICADOR DESDE expresion HASTA expresion HACER declaraciones FIN_PARA','sentencia_para',9,'p_sentencia_para','Parser.py',90),
  ('sentencia_para -> PARA IDENTIFICADOR DESDE expresion HASTA expresion CON_PASO expresion HACER declaraciones FIN_PARA','sentencia_para',11,'p_sentencia_para','Parser.py',91),
  ('sentencia_repetir -> REPETIR declaraciones HASTA_QUE PARENTESIS_IZQ expresion PARENTESIS_DER PUNTO_COMA','sentencia_repetir',7,'p_sentencia_repetir','Parser.py',119),
  ('sentencia_mostrar -> MOSTRAR lista_expresiones PUNTO_COMA','sentencia_mostrar',3,'p_sentencia_mostrar','Parser.py',131),
  ('expresion -> LITERAL_ENTERO','expresion',1,'p_expresion','Parser.py',141),
  ('expresion -> LITERAL_DECIMAL','expresion',1,'p_expresion','Parser.py',142),
  ('expresion -> LITERAL_CADENA','expresion',1,'p_expresion','Parser.py',143),
  ('expresion -> LITERAL_BOOLEANO','expresion',1,'p_expresion','Parser.py',144),
  ('expresion -> IDENTIFICADOR','expresion',1,'p_expresion','Parser.py',145),
  ('expresion -> expresion SUMA expresion','expresion',3,'p_expresion','Parser.py',146),
  ('expresion -> expresion RESTA expresion','expresion',3,'p_expresion','Parser.py',147),
  ('expresion -> expresion MULTIPLICACION expresion','expresion',3,'p_expresion','Parser.py',148),
  ('expresion -> expresion DIVISION expresion','expresion',3,'p_expresion','Parser.py',149),
  ('expresion -> expresion AND expresion','expresion',3,'p_expresion','Parser.py',150),
  ('expresion -> expresion OR expresion','expresion',3,'p_expresion','Parser.py',151),
  ('expresion -> NOT expresion','expresion',2,'p_expresion','Parser.py',152),
  ('expresion -> expresion MAYOR_QUE expresion','expresion',3,'p_expresion','Parser.py',153),
  ('expresion -> expresion MENOR_QUE expresion','expresion',3,'p_expresion','Parser.py',154),
  ('expresion -> expresion MAYOR_IGUAL expresion','expresion',3,'p_expresion','Parser.py',155),
  ('expresion -> expresion MENOR_IGUAL expresion','expresion',3,'p_expresion','Parser.py',156),
  ('expresion -> expresion IGUAL_IGUAL expresion','expresion',3,'p_expresion','Parser.py',157),
  ('expresion -> expresion DIFERENTE expresion','expresion',3,'p_expresion','Parser.py',158),
  ('expresion -> PARENTESIS_IZQ expresion PARENTESIS_DER','expresion',3,'p_expresion','Parser.py',159),
  ('lista_expresiones -> lista_expresiones COMA expresion','lista_expresiones',3,'p_lista_expresiones','Parser.py',205),
  ('lista_expresiones -> expresion','lista_expresiones',1,'p_lista_expresiones','Parser.py',206),
  ('declaracion_simple -> TIPO IDENTIFICADOR PUNTO_COMA','declaracion_simple',3,'p_declaracion_simple','Parser.py',217),
  ('declaracion_con_asignacion -> TIPO IDENTIFICADOR ASIGNACION expresion PUNTO_COMA','declaracion_con_asignacion',5,'p_declaracion_con_asignacion','Parser.py',228),
  ('asignacion -> IDENTIFICADOR ASIGNACION expresion PUNTO_COMA','asignacion',4,'p_asignacion','Parser.py',251),
  ('constante -> TIPO IDENTIFICADOR ASIGNACION expresion','constante',4,'p_constante','Parser.py',273),
]
