# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm as Form
from wtforms import BooleanField, SubmitField, SelectField
from wtforms.validators import Required, DataRequired



class LoadForm(Form):

    load1 = BooleanField('Нагрузка 1')
    load2 = BooleanField('Нагрузка 2')
    load3 = BooleanField('Нагрузка 3')
    point_id = SelectField(u'POINTNAME')
    submit = SubmitField('Выбрать')


def fewPoint(dbClass):

    point = dbClass.query.all()
    form = LoadForm()
    form.point_id.choices = [(g.id, g.pointname) for g in point]
    return form


class BtnAttribute():

    btnPrimaryClass= "btn btn-primary waves-effect waves-light"
    btnSuccessClass = "btn btn-success waves-effect waves-light"
    btnChoicesClass = {"0": btnPrimaryClass, "1": btnSuccessClass}
    btnValue = {"0": "0", "1": "1"}

    def __init__(self,state1,state2,state3):
        self.btnClass1 = self.btnChoicesClass[state1]
        self.btnClass2 = self.btnChoicesClass[state2]
        self.btnClass3 = self.btnChoicesClass[state3]
        self.btnValue1 = self.btnValue[state1]
        self.btnValue2 = self.btnValue[state2]
        self.btnValue3 = self.btnValue[state3]
    
    def update(self,state1,state2,state3):
        self.btnClass1 = self.btnChoicesClass[state1]
        self.btnClass2 = self.btnChoicesClass[state2]
        self.btnClass3 = self.btnChoicesClass[state3]
        self.btnValue1 = self.btnValue[state1]
        self.btnValue2 = self.btnValue[state2]
        self.btnValue3 = self.btnValue[state3]


class BadgeAttribute():

    badgeLightClass = "badge badge-light"
    badgeWarningClass = "badge badge-warning"
    choicesBadgeClass = {"0": badgeLightClass, "1": badgeWarningClass}


    def __init__(self,state1,state2,state3,state4):

        self.badgeClass1 = self.choicesBadgeClass[state1]
        self.badgeClass2 = self.choicesBadgeClass[state2]
        self.badgeClass3 = self.choicesBadgeClass[state3]
        self.badgeClass4 = self.choicesBadgeClass[state4]

    def update(self,state1,state2,state3,state4):

        self.badgeClass1 = self.choicesBadgeClass[state1]
        self.badgeClass2 = self.choicesBadgeClass[state2]
        self.badgeClass3 = self.choicesBadgeClass[state3]
        self.badgeClass4 = self.choicesBadgeClass[state4]