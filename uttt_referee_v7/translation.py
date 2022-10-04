__all__ = ['translation']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['game', 'gameAnalysis', 'computeWinOrLoss', 'MOVEMULTIPLIER', 'minimax', 'calculateLocalPosition', 'computerVal', 'realEvaluateSquare', 'MOVES', 'SCORINGSYSTEM', 'player', 'WINNUM'])
@Js
def PyJsHoisted_computeWinOrLoss_(localBoard, this, arguments, var=var):
    var = Scope({'localBoard':localBoard, 'this':this, 'arguments':arguments}, var)
    var.registers(['localBoard', 'winVal'])
    var.put('winVal', Js(1.0))
    def PyJs_LONG_1_(var=var):
        def PyJs_LONG_0_(var=var):
            return ((PyJsStrictEq(((var.get('localBoard').get('0')+var.get('localBoard').get('1'))+var.get('localBoard').get('2')),(var.get('winVal')*Js(3.0))) or PyJsStrictEq(((var.get('localBoard').get('3')+var.get('localBoard').get('4'))+var.get('localBoard').get('5')),(var.get('winVal')*Js(3.0)))) or PyJsStrictEq(((var.get('localBoard').get('6')+var.get('localBoard').get('7'))+var.get('localBoard').get('8')),(var.get('winVal')*Js(3.0))))
        return (((PyJs_LONG_0_() or PyJsStrictEq(((var.get('localBoard').get('0')+var.get('localBoard').get('3'))+var.get('localBoard').get('6')),(var.get('winVal')*Js(3.0)))) or PyJsStrictEq(((var.get('localBoard').get('1')+var.get('localBoard').get('4'))+var.get('localBoard').get('7')),(var.get('winVal')*Js(3.0)))) or PyJsStrictEq(((var.get('localBoard').get('2')+var.get('localBoard').get('5'))+var.get('localBoard').get('8')),(var.get('winVal')*Js(3.0))))
    if ((PyJs_LONG_1_() or PyJsStrictEq(((var.get('localBoard').get('0')+var.get('localBoard').get('4'))+var.get('localBoard').get('8')),(var.get('winVal')*Js(3.0)))) or PyJsStrictEq(((var.get('localBoard').get('2')+var.get('localBoard').get('4'))+var.get('localBoard').get('6')),(var.get('winVal')*Js(3.0)))):
        return var.get('winVal')
    else:
        def PyJs_LONG_3_(var=var):
            def PyJs_LONG_2_(var=var):
                return ((PyJsStrictEq(((var.get('localBoard').get('0')+var.get('localBoard').get('1'))+var.get('localBoard').get('2')),(var.get('winVal')*Js(3.0))) or PyJsStrictEq(((var.get('localBoard').get('3')+var.get('localBoard').get('4'))+var.get('localBoard').get('5')),(var.get('winVal')*Js(3.0)))) or PyJsStrictEq(((var.get('localBoard').get('6')+var.get('localBoard').get('7'))+var.get('localBoard').get('8')),(var.get('winVal')*Js(3.0))))
            return (((PyJs_LONG_2_() or PyJsStrictEq(((var.get('localBoard').get('0')+var.get('localBoard').get('3'))+var.get('localBoard').get('6')),(var.get('winVal')*Js(3.0)))) or PyJsStrictEq(((var.get('localBoard').get('1')+var.get('localBoard').get('4'))+var.get('localBoard').get('7')),(var.get('winVal')*Js(3.0)))) or PyJsStrictEq(((var.get('localBoard').get('2')+var.get('localBoard').get('5'))+var.get('localBoard').get('8')),(var.get('winVal')*Js(3.0))))
        if ((PyJs_LONG_3_() or PyJsStrictEq(((var.get('localBoard').get('0')+var.get('localBoard').get('4'))+var.get('localBoard').get('8')),(var.get('winVal')*Js(3.0)))) or PyJsStrictEq(((var.get('localBoard').get('2')+var.get('localBoard').get('4'))+var.get('localBoard').get('6')),(var.get('winVal')*Js(3.0)))):
            var.put('winVal', (-Js(1.0)))
            return var.get('winVal')
        else:
            return Js(0.0)
PyJsHoisted_computeWinOrLoss_.func_name = 'computeWinOrLoss'
var.put('computeWinOrLoss', PyJsHoisted_computeWinOrLoss_)
@Js
def PyJsHoisted_gameAnalysis_(tryPos, localBoardNum, this, arguments, var=var):
    var = Scope({'tryPos':tryPos, 'localBoardNum':localBoardNum, 'this':this, 'arguments':arguments}, var)
    var.registers(['localBoardNum', 'count', 'numEval', 'globalBoard', 'tryPos', 'tmpEv'])
    var.put('numEval', Js(0.0))
    var.put('globalBoard', Js([]))
    #for JS loop
    var.put('count', Js(0.0))
    while (var.get('count')<Js(9.0)):
        try:
            var.put('numEval', ((var.get('realEvaluateSquare')(var.get('tryPos').get(var.get('count')))*Js(1.5))*var.get('MOVEMULTIPLIER').get(var.get('count'))), '+')
            if PyJsStrictEq(var.get('count'),var.get('localBoardNum')):
                var.put('numEval', (var.get('realEvaluateSquare')(var.get('tryPos').get(var.get('count')))*var.get('MOVEMULTIPLIER').get(var.get('count'))), '+')
            var.put('tmpEv', var.get('computeWinOrLoss')(var.get('tryPos').get(var.get('count'))))
            var.put('numEval', (var.get('tmpEv')*var.get('MOVEMULTIPLIER').get(var.get('count'))), '-')
            var.get('globalBoard').callprop('push', var.get('tmpEv'))
        finally:
                (var.put('count',Js(var.get('count').to_number())+Js(1))-Js(1))
    var.put('numEval', (var.get('computeWinOrLoss')(var.get('globalBoard'))*var.get('WINNUM')), '-')
    var.put('numEval', (var.get('realEvaluateSquare')(var.get('globalBoard'))*Js(150.0)), '+')
    return var.get('numEval')
PyJsHoisted_gameAnalysis_.func_name = 'gameAnalysis'
var.put('gameAnalysis', PyJsHoisted_gameAnalysis_)
@Js
def PyJsHoisted_minimax_(potenGlobalBoard, boardNum, depth, a, b, minMaxBool, this, arguments, var=var):
    var = Scope({'potenGlobalBoard':potenGlobalBoard, 'boardNum':boardNum, 'depth':depth, 'a':a, 'b':b, 'minMaxBool':minMaxBool, 'this':this, 'arguments':arguments}, var)
    var.registers(['minimaxCount', 'gameEvaluation', 'minMaxBool', 'boardNum', 'boardLoc', 'beginMove', 'minimaxEval', 'minEval', 'b', 'potenGlobalBoard', 'a', 'maxEval', 'depth', 'mMEGE'])
    var.put('beginMove', (-Js(1.0)))
    var.put('gameEvaluation', var.get('gameAnalysis')(var.get('potenGlobalBoard'), var.get('boardNum')))
    if ((var.get('Math').callprop('abs', var.get('gameEvaluation'))>var.get('WINNUM')) or (var.get('depth')<=Js(0.0))):
        return Js({'game_eval':var.get('gameEvaluation'),'move':var.get('beginMove')})
    if (PyJsStrictNeq(var.get('boardNum'),(-Js(1.0))) and PyJsStrictNeq(var.get('computeWinOrLoss')(var.get('potenGlobalBoard').get(var.get('boardNum'))),Js(0.0))):
        var.put('boardNum', (-Js(1.0)))
    else:
        if (PyJsStrictNeq(var.get('boardNum'),(-Js(1.0))) and var.get('potenGlobalBoard').get(var.get('boardNum')).callprop('includes', Js(0.0)).neg()):
            var.put('boardNum', (-Js(1.0)))
    if var.get('minMaxBool'):
        var.put('maxEval', (-var.get('Infinity')))
        #for JS loop
        var.put('minimaxCount', Js(0.0))
        while (var.get('minimaxCount')<Js(9.0)):
            try:
                var.put('minimaxEval', (-var.get('Infinity')))
                if PyJsStrictEq(var.get('boardNum'),(-Js(1.0))):
                    #for JS loop
                    var.put('boardLoc', Js(0.0))
                    while (var.get('boardLoc')<Js(9.0)):
                        try:
                            if PyJsStrictEq(var.get('computeWinOrLoss')(var.get('potenGlobalBoard').get(var.get('minimaxCount'))),Js(0.0)):
                                if PyJsStrictEq(var.get('potenGlobalBoard').get(var.get('minimaxCount')).get(var.get('boardLoc')),Js(0.0)):
                                    var.get('potenGlobalBoard').get(var.get('minimaxCount')).put(var.get('boardLoc'), var.get('computerVal'))
                                    var.put('minimaxEval', var.get('minimax')(var.get('potenGlobalBoard'), var.get('boardLoc'), (var.get('depth')-Js(1.0)), var.get('a'), var.get('b'), Js(False)).get('game_eval'))
                                    var.get('potenGlobalBoard').get(var.get('minimaxCount')).put(var.get('boardLoc'), Js(0.0))
                                if (var.get('minimaxEval')>var.get('maxEval')):
                                    var.put('maxEval', var.get('minimaxEval'))
                                    var.put('beginMove', var.get('minimaxCount'))
                                var.put('a', var.get('Math').callprop('max', var.get('a'), var.get('minimaxEval')))
                        finally:
                                (var.put('boardLoc',Js(var.get('boardLoc').to_number())+Js(1))-Js(1))
                    if (var.get('b')<=var.get('a')):
                        break
                else:
                    if PyJsStrictEq(var.get('potenGlobalBoard').get(var.get('boardNum')).get(var.get('minimaxCount')),Js(0.0)):
                        var.get('potenGlobalBoard').get(var.get('boardNum')).put(var.get('minimaxCount'), var.get('computerVal'))
                        var.put('minimaxEval', var.get('minimax')(var.get('potenGlobalBoard'), var.get('minimaxCount'), (var.get('depth')-Js(1.0)), var.get('a'), var.get('b'), Js(False)))
                        var.get('potenGlobalBoard').get(var.get('boardNum')).put(var.get('minimaxCount'), Js(0.0))
                    var.put('mMEGE', var.get('minimaxEval').get('game_eval'))
                    if (var.get('mMEGE')>var.get('maxEval')):
                        var.put('maxEval', var.get('mMEGE'))
                        var.put('beginMove', var.get('minimaxEval').get('move'))
                    var.put('a', var.get('Math').callprop('max', var.get('a'), var.get('mMEGE')))
                    if (var.get('b')<=var.get('a')):
                        break
            finally:
                    (var.put('minimaxCount',Js(var.get('minimaxCount').to_number())+Js(1))-Js(1))
        return Js({'game_eval':var.get('maxEval'),'move':var.get('beginMove')})
    else:
        var.put('minEval', var.get('Infinity'))
        #for JS loop
        var.put('minimaxCount', Js(0.0))
        while (var.get('minimaxCount')<Js(9.0)):
            try:
                var.put('minimaxEval', var.get('Infinity'))
                if PyJsStrictEq(var.get('boardNum'),(-Js(1.0))):
                    #for JS loop
                    var.put('boardLoc', Js(0.0))
                    while (var.get('boardLoc')<Js(9.0)):
                        try:
                            if PyJsStrictEq(var.get('computeWinOrLoss')(var.get('potenGlobalBoard').get(var.get('minimaxCount'))),Js(0.0)):
                                if PyJsStrictEq(var.get('potenGlobalBoard').get(var.get('minimaxCount')).get(var.get('boardLoc')),Js(0.0)):
                                    var.get('potenGlobalBoard').get(var.get('minimaxCount')).put(var.get('boardLoc'), var.get('player'))
                                    var.put('minimaxEval', var.get('minimax')(var.get('potenGlobalBoard'), var.get('boardLoc'), (var.get('depth')-Js(1.0)), var.get('a'), var.get('b'), Js(True)).get('game_eval'))
                                    var.get('potenGlobalBoard').get(var.get('minimaxCount')).put(var.get('boardLoc'), Js(0.0))
                                if (var.get('minimaxEval')<var.get('minEval')):
                                    var.put('minEval', var.get('minimaxEval'))
                                    var.put('beginMove', var.get('minimaxCount'))
                                var.put('b', var.get('Math').callprop('min', var.get('b'), var.get('minimaxEval')))
                        finally:
                                (var.put('boardLoc',Js(var.get('boardLoc').to_number())+Js(1))-Js(1))
                    if (var.get('b')<=var.get('a')):
                        break
                else:
                    if PyJsStrictEq(var.get('potenGlobalBoard').get(var.get('boardNum')).get(var.get('minimaxCount')),Js(0.0)):
                        var.get('potenGlobalBoard').get(var.get('boardNum')).put(var.get('minimaxCount'), var.get('player'))
                        var.put('minimaxEval', var.get('minimax')(var.get('potenGlobalBoard'), var.get('minimaxCount'), (var.get('depth')-Js(1.0)), var.get('a'), var.get('b'), Js(True)))
                        var.get('potenGlobalBoard').get(var.get('boardNum')).put(var.get('minimaxCount'), Js(0.0))
                    var.put('mMEGE', var.get('minimaxEval').get('game_eval'))
                    if (var.get('mMEGE')<var.get('minEval')):
                        var.put('minEval', var.get('mMEGE'))
                        var.put('beginMove', var.get('minimaxEval').get('move'))
                    var.put('b', var.get('Math').callprop('min', var.get('b'), var.get('mMEGE')))
                    if (var.get('b')<=var.get('a')):
                        break
            finally:
                    (var.put('minimaxCount',Js(var.get('minimaxCount').to_number())+Js(1))-Js(1))
        return Js({'game_eval':var.get('minEval'),'move':var.get('beginMove')})
PyJsHoisted_minimax_.func_name = 'minimax'
var.put('minimax', PyJsHoisted_minimax_)
@Js
def PyJsHoisted_calculateLocalPosition_(localBoard, boardNum, this, arguments, var=var):
    var = Scope({'localBoard':localBoard, 'boardNum':boardNum, 'this':this, 'arguments':arguments}, var)
    var.registers(['localBoard', 'a', 'evaluation', 'boardNum'])
    var.get('localBoard').put(var.get('boardNum'), var.get('computerVal'))
    var.put('evaluation', Js(0.0))
    var.put('a', Js(2.0))
    var.put('evaluation', var.get('SCORINGSYSTEM').get(var.get('boardNum')), '+')
    var.put('a', (-Js(2.0)))
    def PyJs_LONG_5_(var=var):
        def PyJs_LONG_4_(var=var):
            return (((PyJsStrictEq(((var.get('localBoard').get('0')+var.get('localBoard').get('1'))+var.get('localBoard').get('2')),var.get('a')) or PyJsStrictEq(((var.get('localBoard').get('3')+var.get('localBoard').get('4'))+var.get('localBoard').get('5')),var.get('a'))) or PyJsStrictEq(((var.get('localBoard').get('6')+var.get('localBoard').get('7'))+var.get('localBoard').get('8')),var.get('a'))) or PyJsStrictEq(((var.get('localBoard').get('0')+var.get('localBoard').get('3'))+var.get('localBoard').get('6')),var.get('a')))
        return (((PyJs_LONG_4_() or PyJsStrictEq(((var.get('localBoard').get('1')+var.get('localBoard').get('4'))+var.get('localBoard').get('7')),var.get('a'))) or PyJsStrictEq(((var.get('localBoard').get('2')+var.get('localBoard').get('5'))+var.get('localBoard').get('8')),var.get('a'))) or PyJsStrictEq(((var.get('localBoard').get('0')+var.get('localBoard').get('4'))+var.get('localBoard').get('8')),var.get('a')))
    if (PyJs_LONG_5_() or PyJsStrictEq(((var.get('localBoard').get('2')+var.get('localBoard').get('4'))+var.get('localBoard').get('6')),var.get('a'))):
        var.put('evaluation', Js(1.0), '+')
    var.put('a', (-Js(3.0)))
    def PyJs_LONG_7_(var=var):
        def PyJs_LONG_6_(var=var):
            return (((PyJsStrictEq(((var.get('localBoard').get('0')+var.get('localBoard').get('1'))+var.get('localBoard').get('2')),var.get('a')) or PyJsStrictEq(((var.get('localBoard').get('3')+var.get('localBoard').get('4'))+var.get('localBoard').get('5')),var.get('a'))) or PyJsStrictEq(((var.get('localBoard').get('6')+var.get('localBoard').get('7'))+var.get('localBoard').get('8')),var.get('a'))) or PyJsStrictEq(((var.get('localBoard').get('0')+var.get('localBoard').get('3'))+var.get('localBoard').get('6')),var.get('a')))
        return (((PyJs_LONG_6_() or PyJsStrictEq(((var.get('localBoard').get('1')+var.get('localBoard').get('4'))+var.get('localBoard').get('7')),var.get('a'))) or PyJsStrictEq(((var.get('localBoard').get('2')+var.get('localBoard').get('5'))+var.get('localBoard').get('8')),var.get('a'))) or PyJsStrictEq(((var.get('localBoard').get('0')+var.get('localBoard').get('4'))+var.get('localBoard').get('8')),var.get('a')))
    if (PyJs_LONG_7_() or PyJsStrictEq(((var.get('localBoard').get('2')+var.get('localBoard').get('4'))+var.get('localBoard').get('6')),var.get('a'))):
        var.put('evaluation', Js(5.0), '+')
    var.get('localBoard').put(var.get('boardNum'), var.get('player'))
    var.put('a', Js(3.0))
    def PyJs_LONG_9_(var=var):
        def PyJs_LONG_8_(var=var):
            return (((PyJsStrictEq(((var.get('localBoard').get('0')+var.get('localBoard').get('1'))+var.get('localBoard').get('2')),var.get('a')) or PyJsStrictEq(((var.get('localBoard').get('3')+var.get('localBoard').get('4'))+var.get('localBoard').get('5')),var.get('a'))) or PyJsStrictEq(((var.get('localBoard').get('6')+var.get('localBoard').get('7'))+var.get('localBoard').get('8')),var.get('a'))) or PyJsStrictEq(((var.get('localBoard').get('0')+var.get('localBoard').get('3'))+var.get('localBoard').get('6')),var.get('a')))
        return (((PyJs_LONG_8_() or PyJsStrictEq(((var.get('localBoard').get('1')+var.get('localBoard').get('4'))+var.get('localBoard').get('7')),var.get('a'))) or PyJsStrictEq(((var.get('localBoard').get('2')+var.get('localBoard').get('5'))+var.get('localBoard').get('8')),var.get('a'))) or PyJsStrictEq(((var.get('localBoard').get('0')+var.get('localBoard').get('4'))+var.get('localBoard').get('8')),var.get('a')))
    if (PyJs_LONG_9_() or PyJsStrictEq(((var.get('localBoard').get('2')+var.get('localBoard').get('4'))+var.get('localBoard').get('6')),var.get('a'))):
        var.put('evaluation', Js(2.0), '+')
    var.get('localBoard').put(var.get('boardNum'), var.get('computerVal'))
    var.put('evaluation', (var.get('computeWinOrLoss')(var.get('localBoard'))*Js(15.0)), '-')
    var.get('localBoard').put(var.get('boardNum'), Js(0.0))
    return var.get('evaluation')
PyJsHoisted_calculateLocalPosition_.func_name = 'calculateLocalPosition'
var.put('calculateLocalPosition', PyJsHoisted_calculateLocalPosition_)
@Js
def PyJsHoisted_realEvaluateSquare_(possLocalBoard, this, arguments, var=var):
    var = Scope({'possLocalBoard':possLocalBoard, 'this':this, 'arguments':arguments}, var)
    var.registers(['comparison', 'index', 'evaluation', 'possLocalBoard'])
    var.put('evaluation', Js(0.0))
    for PyJsTemp in var.get('possLocalBoard'):
        var.put('index', PyJsTemp)
        var.put('evaluation', (var.get('possLocalBoard').get(var.get('index'))*var.get('SCORINGSYSTEM').get(var.get('index'))), '-')
    var.put('comparison', Js(2.0))
    def PyJs_LONG_10_(var=var):
        return ((PyJsStrictEq(((var.get('possLocalBoard').get('0')+var.get('possLocalBoard').get('1'))+var.get('possLocalBoard').get('2')),var.get('comparison')) or PyJsStrictEq(((var.get('possLocalBoard').get('3')+var.get('possLocalBoard').get('4'))+var.get('possLocalBoard').get('5')),var.get('comparison'))) or PyJsStrictEq(((var.get('possLocalBoard').get('6')+var.get('possLocalBoard').get('7'))+var.get('possLocalBoard').get('8')),var.get('comparison')))
    if PyJs_LONG_10_():
        var.put('evaluation', Js(6.0), '-')
    def PyJs_LONG_11_(var=var):
        return ((PyJsStrictEq(((var.get('possLocalBoard').get('0')+var.get('possLocalBoard').get('3'))+var.get('possLocalBoard').get('6')),var.get('comparison')) or PyJsStrictEq(((var.get('possLocalBoard').get('1')+var.get('possLocalBoard').get('4'))+var.get('possLocalBoard').get('7')),var.get('comparison'))) or PyJsStrictEq(((var.get('possLocalBoard').get('2')+var.get('possLocalBoard').get('5'))+var.get('possLocalBoard').get('8')),var.get('comparison')))
    if PyJs_LONG_11_():
        var.put('evaluation', Js(6.0), '-')
    if (PyJsStrictEq(((var.get('possLocalBoard').get('0')+var.get('possLocalBoard').get('4'))+var.get('possLocalBoard').get('8')),var.get('comparison')) or PyJsStrictEq(((var.get('possLocalBoard').get('2')+var.get('possLocalBoard').get('4'))+var.get('possLocalBoard').get('6')),var.get('comparison'))):
        var.put('evaluation', Js(7.0), '-')
    var.put('comparison', (-Js(1.0)))
    def PyJs_LONG_22_(var=var):
        def PyJs_LONG_21_(var=var):
            def PyJs_LONG_20_(var=var):
                def PyJs_LONG_19_(var=var):
                    def PyJs_LONG_18_(var=var):
                        def PyJs_LONG_17_(var=var):
                            def PyJs_LONG_16_(var=var):
                                def PyJs_LONG_15_(var=var):
                                    def PyJs_LONG_14_(var=var):
                                        def PyJs_LONG_13_(var=var):
                                            def PyJs_LONG_12_(var=var):
                                                return (((PyJsStrictEq((var.get('possLocalBoard').get('0')+var.get('possLocalBoard').get('1')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('2'),(-var.get('comparison')))) or (PyJsStrictEq((var.get('possLocalBoard').get('1')+var.get('possLocalBoard').get('2')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('0'),(-var.get('comparison'))))) or (PyJsStrictEq((var.get('possLocalBoard').get('0')+var.get('possLocalBoard').get('2')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('1'),(-var.get('comparison')))))
                                            return ((PyJs_LONG_12_() or (PyJsStrictEq((var.get('possLocalBoard').get('3')+var.get('possLocalBoard').get('4')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('5'),(-var.get('comparison'))))) or (PyJsStrictEq((var.get('possLocalBoard').get('3')+var.get('possLocalBoard').get('5')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('4'),(-var.get('comparison')))))
                                        return ((PyJs_LONG_13_() or (PyJsStrictEq((var.get('possLocalBoard').get('5')+var.get('possLocalBoard').get('4')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('3'),(-var.get('comparison'))))) or (PyJsStrictEq((var.get('possLocalBoard').get('6')+var.get('possLocalBoard').get('7')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('8'),(-var.get('comparison')))))
                                    return ((PyJs_LONG_14_() or (PyJsStrictEq((var.get('possLocalBoard').get('6')+var.get('possLocalBoard').get('8')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('7'),(-var.get('comparison'))))) or (PyJsStrictEq((var.get('possLocalBoard').get('7')+var.get('possLocalBoard').get('8')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('6'),(-var.get('comparison')))))
                                return ((PyJs_LONG_15_() or (PyJsStrictEq((var.get('possLocalBoard').get('0')+var.get('possLocalBoard').get('3')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('6'),(-var.get('comparison'))))) or (PyJsStrictEq((var.get('possLocalBoard').get('0')+var.get('possLocalBoard').get('6')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('3'),(-var.get('comparison')))))
                            return ((PyJs_LONG_16_() or (PyJsStrictEq((var.get('possLocalBoard').get('3')+var.get('possLocalBoard').get('6')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('0'),(-var.get('comparison'))))) or (PyJsStrictEq((var.get('possLocalBoard').get('1')+var.get('possLocalBoard').get('4')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('7'),(-var.get('comparison')))))
                        return ((PyJs_LONG_17_() or (PyJsStrictEq((var.get('possLocalBoard').get('1')+var.get('possLocalBoard').get('7')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('4'),(-var.get('comparison'))))) or (PyJsStrictEq((var.get('possLocalBoard').get('4')+var.get('possLocalBoard').get('7')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('1'),(-var.get('comparison')))))
                    return ((PyJs_LONG_18_() or (PyJsStrictEq((var.get('possLocalBoard').get('2')+var.get('possLocalBoard').get('5')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('8'),(-var.get('comparison'))))) or (PyJsStrictEq((var.get('possLocalBoard').get('2')+var.get('possLocalBoard').get('8')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('5'),(-var.get('comparison')))))
                return ((PyJs_LONG_19_() or (PyJsStrictEq((var.get('possLocalBoard').get('5')+var.get('possLocalBoard').get('8')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('2'),(-var.get('comparison'))))) or (PyJsStrictEq((var.get('possLocalBoard').get('0')+var.get('possLocalBoard').get('4')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('8'),(-var.get('comparison')))))
            return ((PyJs_LONG_20_() or (PyJsStrictEq((var.get('possLocalBoard').get('0')+var.get('possLocalBoard').get('8')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('4'),(-var.get('comparison'))))) or (PyJsStrictEq((var.get('possLocalBoard').get('4')+var.get('possLocalBoard').get('8')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('0'),(-var.get('comparison')))))
        return ((PyJs_LONG_21_() or (PyJsStrictEq((var.get('possLocalBoard').get('2')+var.get('possLocalBoard').get('4')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('6'),(-var.get('comparison'))))) or (PyJsStrictEq((var.get('possLocalBoard').get('2')+var.get('possLocalBoard').get('6')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('4'),(-var.get('comparison')))))
    if (PyJs_LONG_22_() or (PyJsStrictEq((var.get('possLocalBoard').get('4')+var.get('possLocalBoard').get('6')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('2'),(-var.get('comparison'))))):
        var.put('evaluation', Js(9.0), '-')
    var.put('comparison', (-Js(2.0)))
    def PyJs_LONG_23_(var=var):
        return ((PyJsStrictEq(((var.get('possLocalBoard').get('0')+var.get('possLocalBoard').get('1'))+var.get('possLocalBoard').get('2')),var.get('comparison')) or PyJsStrictEq(((var.get('possLocalBoard').get('3')+var.get('possLocalBoard').get('4'))+var.get('possLocalBoard').get('5')),var.get('comparison'))) or PyJsStrictEq(((var.get('possLocalBoard').get('6')+var.get('possLocalBoard').get('7'))+var.get('possLocalBoard').get('8')),var.get('comparison')))
    if PyJs_LONG_23_():
        var.put('evaluation', Js(6.0), '+')
    def PyJs_LONG_24_(var=var):
        return ((PyJsStrictEq(((var.get('possLocalBoard').get('0')+var.get('possLocalBoard').get('3'))+var.get('possLocalBoard').get('6')),var.get('comparison')) or PyJsStrictEq(((var.get('possLocalBoard').get('1')+var.get('possLocalBoard').get('4'))+var.get('possLocalBoard').get('7')),var.get('comparison'))) or PyJsStrictEq(((var.get('possLocalBoard').get('2')+var.get('possLocalBoard').get('5'))+var.get('possLocalBoard').get('8')),var.get('comparison')))
    if PyJs_LONG_24_():
        var.put('evaluation', Js(6.0), '+')
    if (PyJsStrictEq(((var.get('possLocalBoard').get('0')+var.get('possLocalBoard').get('4'))+var.get('possLocalBoard').get('8')),var.get('comparison')) or PyJsStrictEq(((var.get('possLocalBoard').get('2')+var.get('possLocalBoard').get('4'))+var.get('possLocalBoard').get('6')),var.get('comparison'))):
        var.put('evaluation', Js(7.0), '+')
    var.put('comparison', Js(1.0))
    def PyJs_LONG_35_(var=var):
        def PyJs_LONG_34_(var=var):
            def PyJs_LONG_33_(var=var):
                def PyJs_LONG_32_(var=var):
                    def PyJs_LONG_31_(var=var):
                        def PyJs_LONG_30_(var=var):
                            def PyJs_LONG_29_(var=var):
                                def PyJs_LONG_28_(var=var):
                                    def PyJs_LONG_27_(var=var):
                                        def PyJs_LONG_26_(var=var):
                                            def PyJs_LONG_25_(var=var):
                                                return (((PyJsStrictEq((var.get('possLocalBoard').get('0')+var.get('possLocalBoard').get('1')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('2'),(-var.get('comparison')))) or (PyJsStrictEq((var.get('possLocalBoard').get('1')+var.get('possLocalBoard').get('2')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('0'),(-var.get('comparison'))))) or (PyJsStrictEq((var.get('possLocalBoard').get('0')+var.get('possLocalBoard').get('2')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('1'),(-var.get('comparison')))))
                                            return ((PyJs_LONG_25_() or (PyJsStrictEq((var.get('possLocalBoard').get('3')+var.get('possLocalBoard').get('4')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('5'),(-var.get('comparison'))))) or (PyJsStrictEq((var.get('possLocalBoard').get('3')+var.get('possLocalBoard').get('5')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('4'),(-var.get('comparison')))))
                                        return ((PyJs_LONG_26_() or (PyJsStrictEq((var.get('possLocalBoard').get('5')+var.get('possLocalBoard').get('4')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('3'),(-var.get('comparison'))))) or (PyJsStrictEq((var.get('possLocalBoard').get('6')+var.get('possLocalBoard').get('7')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('8'),(-var.get('comparison')))))
                                    return ((PyJs_LONG_27_() or (PyJsStrictEq((var.get('possLocalBoard').get('6')+var.get('possLocalBoard').get('8')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('7'),(-var.get('comparison'))))) or (PyJsStrictEq((var.get('possLocalBoard').get('7')+var.get('possLocalBoard').get('8')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('6'),(-var.get('comparison')))))
                                return ((PyJs_LONG_28_() or (PyJsStrictEq((var.get('possLocalBoard').get('0')+var.get('possLocalBoard').get('3')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('6'),(-var.get('comparison'))))) or (PyJsStrictEq((var.get('possLocalBoard').get('0')+var.get('possLocalBoard').get('6')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('3'),(-var.get('comparison')))))
                            return ((PyJs_LONG_29_() or (PyJsStrictEq((var.get('possLocalBoard').get('3')+var.get('possLocalBoard').get('6')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('0'),(-var.get('comparison'))))) or (PyJsStrictEq((var.get('possLocalBoard').get('1')+var.get('possLocalBoard').get('4')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('7'),(-var.get('comparison')))))
                        return ((PyJs_LONG_30_() or (PyJsStrictEq((var.get('possLocalBoard').get('1')+var.get('possLocalBoard').get('7')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('4'),(-var.get('comparison'))))) or (PyJsStrictEq((var.get('possLocalBoard').get('4')+var.get('possLocalBoard').get('7')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('1'),(-var.get('comparison')))))
                    return ((PyJs_LONG_31_() or (PyJsStrictEq((var.get('possLocalBoard').get('2')+var.get('possLocalBoard').get('5')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('8'),(-var.get('comparison'))))) or (PyJsStrictEq((var.get('possLocalBoard').get('2')+var.get('possLocalBoard').get('8')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('5'),(-var.get('comparison')))))
                return ((PyJs_LONG_32_() or (PyJsStrictEq((var.get('possLocalBoard').get('5')+var.get('possLocalBoard').get('8')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('2'),(-var.get('comparison'))))) or (PyJsStrictEq((var.get('possLocalBoard').get('0')+var.get('possLocalBoard').get('4')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('8'),(-var.get('comparison')))))
            return ((PyJs_LONG_33_() or (PyJsStrictEq((var.get('possLocalBoard').get('0')+var.get('possLocalBoard').get('8')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('4'),(-var.get('comparison'))))) or (PyJsStrictEq((var.get('possLocalBoard').get('4')+var.get('possLocalBoard').get('8')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('0'),(-var.get('comparison')))))
        return ((PyJs_LONG_34_() or (PyJsStrictEq((var.get('possLocalBoard').get('2')+var.get('possLocalBoard').get('4')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('6'),(-var.get('comparison'))))) or (PyJsStrictEq((var.get('possLocalBoard').get('2')+var.get('possLocalBoard').get('6')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('4'),(-var.get('comparison')))))
    if (PyJs_LONG_35_() or (PyJsStrictEq((var.get('possLocalBoard').get('4')+var.get('possLocalBoard').get('6')),(Js(2.0)*var.get('comparison'))) and PyJsStrictEq(var.get('possLocalBoard').get('2'),(-var.get('comparison'))))):
        var.put('evaluation', Js(9.0), '+')
    var.put('evaluation', (var.get('computeWinOrLoss')(var.get('possLocalBoard'))*Js(12.0)), '-')
    return var.get('evaluation')
PyJsHoisted_realEvaluateSquare_.func_name = 'realEvaluateSquare'
var.put('realEvaluateSquare', PyJsHoisted_realEvaluateSquare_)
@Js
def PyJsHoisted_game_(playerName, smallBoards, currBoard, pyScript, this, arguments, var=var):
    var = Scope({'playerName':playerName, 'smallBoards':smallBoards, 'currBoard':currBoard, 'pyScript':pyScript, 'this':this, 'arguments':arguments}, var)
    var.registers(['temp', 'currBoard', 'numCount', 'y', 'x', 'playerName', 'count', 'boardCount', 'index', 'analysis', 'smallBoards', 'cachedMiniMax', 'pyScript', 'finalBoard', 'currentBoard'])
    if var.get('pyScript'):
        @Js
        def PyJs_anonymous_36_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            var.get('Array')(Js(9.0)).callprop('fill', Js(0.0))
        PyJs_anonymous_36_._set_name('anonymous')
        var.put('finalBoard', var.get('Array')(Js(9.0)).callprop('fill').callprop('map', PyJs_anonymous_36_))
        var.put('smallBoards', (Js('')+var.get('smallBoards')))
        var.put('boardCount', Js(0.0))
        var.put('numCount', Js(0.0))
        #for JS loop
        var.put('x', Js(0.0))
        while (var.get('x')<var.get('smallBoards').get('length')):
            try:
                if (var.get('numCount')>=Js(9.0)):
                    var.put('boardCount', Js(1.0), '+')
                    var.put('numCount', Js(9.0), '-')
                if PyJsStrictEq(var.get('smallBoards').callprop('substring', var.get('x'), (var.get('x')+Js(1.0))),Js('-')):
                    var.get('finalBoard').get(var.get('boardCount')).put(var.get('numCount'), var.get('smallBoards').callprop('substring', var.get('x'), (var.get('x')+Js(2.0))))
                    var.put('x', Js(1.0), '+')
                    var.put('numCount', Js(1.0), '+')
                else:
                    if (PyJsStrictEq(var.get('smallBoards').callprop('substring', var.get('x'), (var.get('x')+Js(1.0))),Js('0')) or PyJsStrictEq(var.get('smallBoards').callprop('substring', var.get('x'), (var.get('x')+Js(1.0))),Js('1'))):
                        var.get('finalBoard').get(var.get('boardCount')).put(var.get('numCount'), var.get('smallBoards').callprop('substring', var.get('x'), (var.get('x')+Js(1.0))))
                        var.put('numCount', Js(1.0), '+')
            finally:
                    (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
        #for JS loop
        var.put('x', Js(0.0))
        while (var.get('x')<Js(9.0)):
            try:
                #for JS loop
                var.put('y', Js(0.0))
                while (var.get('y')<Js(9.0)):
                    try:
                        var.get('finalBoard').get(var.get('x')).put(var.get('y'), (+var.get('finalBoard').get(var.get('x')).get(var.get('y'))))
                    finally:
                            (var.put('y',Js(var.get('y').to_number())+Js(1))-Js(1))
            finally:
                    (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
        var.put('smallBoards', var.get('finalBoard'))
    var.put('currentBoard', var.get('currBoard'))
    var.put('topMove', (-Js(1.0)))
    var.put('topScore', Js([(-var.get('Infinity')), (-var.get('Infinity')), (-var.get('Infinity')), (-var.get('Infinity')), (-var.get('Infinity')), (-var.get('Infinity')), (-var.get('Infinity')), (-var.get('Infinity')), (-var.get('Infinity'))]))
    var.put('count', Js(0.0))
    #for JS loop
    var.put('index', Js(0.0))
    while (var.get('index')<var.get('smallBoards').get('length')):
        try:
            if PyJsStrictEq(var.get('computeWinOrLoss')(var.get('smallBoards').get(var.get('index'))),Js(0.0)):
                @Js
                def PyJs_anonymous_37_(param, this, arguments, var=var):
                    var = Scope({'param':param, 'this':this, 'arguments':arguments}, var)
                    var.registers(['param'])
                    (PyJsStrictEq(var.get('param'),Js(0.0)) and (var.put('count',Js(var.get('count').to_number())+Js(1))-Js(1)))
                PyJs_anonymous_37_._set_name('anonymous')
                var.get('smallBoards').get(var.get('index')).callprop('forEach', PyJs_anonymous_37_)
        finally:
                (var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))
    if (PyJsStrictNeq(var.get('computeWinOrLoss')(var.get('smallBoards').get(var.get('currentBoard'))),Js(0.0)) or PyJsStrictEq(var.get('currentBoard'),(-Js(1.0)))):
        pass
        if (var.get('MOVES')<Js(10.0)):
            var.put('cachedMiniMax', var.get('minimax')(var.get('smallBoards'), (-Js(1.0)), var.get('Math').callprop('min', Js(4.0), var.get('count')), (-var.get('Infinity')), var.get('Infinity'), Js(True)))
        else:
            if (var.get('MOVES')<Js(18.0)):
                var.put('cachedMiniMax', var.get('minimax')(var.get('smallBoards'), (-Js(1.0)), var.get('Math').callprop('min', Js(5.0), var.get('count')), (-var.get('Infinity')), var.get('Infinity'), Js(True)))
            else:
                var.put('cachedMiniMax', var.get('minimax')(var.get('smallBoards'), (-Js(1.0)), var.get('Math').callprop('min', Js(6.0), var.get('count')), (-var.get('Infinity')), var.get('Infinity'), Js(True)))
        var.put('currentBoard', var.get('cachedMiniMax').get('move'))
    #for JS loop
    var.put('index', Js(0.0))
    while (var.get('index')<Js(9.0)):
        try:
            if PyJsStrictEq(var.get('smallBoards').get(var.get('currentBoard')).get(var.get('index')),Js(0.0)):
                var.put('topMove', var.get('index'))
                break
        finally:
                (var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))
    if PyJsStrictNeq(var.get('topMove'),(-Js(1.0))):
        #for JS loop
        var.put('index', Js(0.0))
        while (var.get('index')<Js(9.0)):
            try:
                if PyJsStrictEq(var.get('smallBoards').get(var.get('currentBoard')).get(var.get('index')),Js(0.0)):
                    var.put('analysis', (var.get('calculateLocalPosition')(var.get('smallBoards').get(var.get('currentBoard')), var.get('index'))*Js(45.0)))
                    var.get('topScore').put(var.get('index'), var.get('analysis'))
            finally:
                    (var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))
        #for JS loop
        var.put('index', Js(0.0))
        while (var.get('index')<Js(9.0)):
            try:
                if PyJsStrictEq(var.get('computeWinOrLoss')(var.get('smallBoards').get(var.get('currentBoard'))),Js(0.0)):
                    if PyJsStrictEq(var.get('smallBoards').get(var.get('currentBoard')).get(var.get('index')),Js(0.0)):
                        var.get('smallBoards').get(var.get('currentBoard')).put(var.get('index'), var.get('computerVal'))
                        pass
                        if (var.get('MOVES')<Js(20.0)):
                            var.put('cachedMiniMax', var.get('minimax')(var.get('smallBoards'), var.get('index'), var.get('Math').callprop('min', Js(5.0), var.get('count')), (-var.get('Infinity')), var.get('Infinity'), Js(False)))
                        else:
                            if (var.get('MOVES')<Js(32.0)):
                                var.put('cachedMiniMax', var.get('minimax')(var.get('smallBoards'), var.get('index'), var.get('Math').callprop('min', Js(6.0), var.get('count')), (-var.get('Infinity')), var.get('Infinity'), Js(False)))
                            else:
                                var.put('cachedMiniMax', var.get('minimax')(var.get('smallBoards'), var.get('index'), var.get('Math').callprop('min', Js(7.0), var.get('count')), (-var.get('Infinity')), var.get('Infinity'), Js(False)))
                        var.put('temp', var.get('cachedMiniMax').get('game_eval'))
                        var.get('smallBoards').get(var.get('currentBoard')).put(var.get('index'), Js(0.0))
                        var.get('topScore').put(var.get('index'), var.get('temp'), '+')
            finally:
                    (var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))
        for PyJsTemp in var.get('topScore'):
            var.put('index', PyJsTemp)
            if (var.get('topScore').get(var.get('index'))>var.get('topScore').get(var.get('topMove'))):
                var.put('topMove', var.get('index'))
        if PyJsStrictEq(var.get('smallBoards').get(var.get('currentBoard')).get(var.get('topMove')),Js(0.0)):
            var.get('smallBoards').get(var.get('currentBoard')).put(var.get('topMove'), var.get('computerVal'))
    return ((((var.get('playerName')+Js(' '))+var.get('currentBoard'))+Js(' '))+var.get('topMove'))
PyJsHoisted_game_.func_name = 'game'
var.put('game', PyJsHoisted_game_)
var.put('player', Js(1.0))
var.put('computerVal', (-Js(1.0)))
var.put('MOVES', Js(0.0))
var.put('MOVEMULTIPLIER', Js([Js(1.4), Js(1.0), Js(1.4), Js(1.0), Js(1.75), Js(1.0), Js(1.4), Js(1.0), Js(1.4)]))
var.put('WINNUM', Js(5000.0))
var.put('SCORINGSYSTEM', Js([Js(0.2), Js(0.17), Js(0.2), Js(0.17), Js(0.22), Js(0.17), Js(0.2), Js(0.17), Js(0.2)]))
pass
pass
pass
pass
pass
pass
pass


# Add lib to the module scope
translation = var.to_python()