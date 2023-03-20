
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMMENTARY HEADER LONG_CASTLE MOVE SHORT_CASTLE TURN TURN_RECOVERY VICTORYlog : gamegame : descriptor play result gamegame : emptydescriptor : HEADER descriptordescriptor : emptyplay : turn playplay : emptyturn : TURN move_p1 com_p1 move_p2 com_p2turn : emptycom_p1 : commentary TURN_RECOVERYcom_p1 : empty\n           com_p2 : commentarycom_p2 : empty\n           commentary : COMMENTARYmove_p1 : MOVE\n                   | LONG_CASTLE\n                   | SHORT_CASTLEmove_p2 : MOVE\n                   | LONG_CASTLE\n                   | SHORT_CASTLEresult : VICTORYempty :'
    
_lr_action_items = {'HEADER':([0,5,12,13,],[5,5,5,-21,]),'$end':([0,1,2,4,12,13,19,],[-22,0,-1,-3,-22,-21,-2,]),'TURN':([0,3,4,5,7,8,10,11,12,13,23,24,25,26,27,29,30,31,],[-22,9,-5,-22,9,-9,-4,-5,-22,-21,-14,-22,-18,-19,-20,-8,-12,-13,]),'VICTORY':([0,3,4,5,6,7,8,10,11,12,13,14,23,24,25,26,27,29,30,31,],[-22,-22,-5,-22,13,-22,-7,-4,-5,-22,-21,-6,-14,-22,-18,-19,-20,-8,-12,-13,]),'MOVE':([9,15,16,17,18,20,22,28,],[16,-22,-15,-16,-17,25,-11,-10,]),'LONG_CASTLE':([9,15,16,17,18,20,22,28,],[17,-22,-15,-16,-17,26,-11,-10,]),'SHORT_CASTLE':([9,15,16,17,18,20,22,28,],[18,-22,-15,-16,-17,27,-11,-10,]),'COMMENTARY':([15,16,17,18,24,25,26,27,],[23,-15,-16,-17,23,-18,-19,-20,]),'TURN_RECOVERY':([21,23,],[28,-14,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'log':([0,],[1,]),'game':([0,12,],[2,19,]),'descriptor':([0,5,12,],[3,10,3,]),'empty':([0,3,5,7,12,15,24,],[4,8,11,8,4,22,31,]),'play':([3,7,],[6,14,]),'turn':([3,7,],[7,7,]),'result':([6,],[12,]),'move_p1':([9,],[15,]),'com_p1':([15,],[20,]),'commentary':([15,24,],[21,30,]),'move_p2':([20,],[24,]),'com_p2':([24,],[29,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> log","S'",1,None,None,None),
  ('log -> game','log',1,'p_log','parser.py',55),
  ('game -> descriptor play result game','game',4,'p_game','parser.py',59),
  ('game -> empty','game',1,'p_game_empty','parser.py',63),
  ('descriptor -> HEADER descriptor','descriptor',2,'p_descriptor','parser.py',67),
  ('descriptor -> empty','descriptor',1,'p_descriptor_empty','parser.py',71),
  ('play -> turn play','play',2,'p_play','parser.py',75),
  ('play -> empty','play',1,'p_play_empty','parser.py',78),
  ('turn -> TURN move_p1 com_p1 move_p2 com_p2','turn',5,'p_turn','parser.py',82),
  ('turn -> empty','turn',1,'p_turn_empty','parser.py',86),
  ('com_p1 -> commentary TURN_RECOVERY','com_p1',2,'p_com_p1','parser.py',90),
  ('com_p1 -> empty','com_p1',1,'p_com_p1_empty','parser.py',94),
  ('com_p2 -> commentary','com_p2',1,'p_com_p2','parser.py',99),
  ('com_p2 -> empty','com_p2',1,'p_com_p2_empty','parser.py',103),
  ('commentary -> COMMENTARY','commentary',1,'p_commentary','parser.py',108),
  ('move_p1 -> MOVE','move_p1',1,'p_move_p1','parser.py',112),
  ('move_p1 -> LONG_CASTLE','move_p1',1,'p_move_p1','parser.py',113),
  ('move_p1 -> SHORT_CASTLE','move_p1',1,'p_move_p1','parser.py',114),
  ('move_p2 -> MOVE','move_p2',1,'p_move_p2','parser.py',119),
  ('move_p2 -> LONG_CASTLE','move_p2',1,'p_move_p2','parser.py',120),
  ('move_p2 -> SHORT_CASTLE','move_p2',1,'p_move_p2','parser.py',121),
  ('result -> VICTORY','result',1,'p_result','parser.py',127),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',134),
]
