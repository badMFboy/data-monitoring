from flask import render_template, request
from app.charts.forms import fewPoint, BtnAttribute, BadgeAttribute
from flask_login import login_required
from app.charts import bp
from app.models import Point


@bp.route('/charts',methods=['GET','POST'])
@login_required
def charts():
    print("yes, know your get charts page")

    form = fewPoint(Point) # create Form for rendering
    loads = BtnAttribute('0','0','0') # create Btns Class for rendering
    badges = BadgeAttribute('0','0','0','0') # create Badges Class for rendering

    if request.method == 'POST':
        state = Point.query.filter_by(id=request.form["point_id"]).first()
        loads.update(state.load1,state.load2,state.load3)
        badges.update(state.digInA,state.digInB,state.digInC,state.digInD)
        return render_template('charts.html',form = form,loads = loads, badges = badges)

    return render_template('charts.html',form = form,loads = loads, badges=badges)
