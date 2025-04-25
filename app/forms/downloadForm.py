from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, HiddenField


class downloadForm(FlaskForm):
    content_type = SelectField(
        'Content Type',
        choices=[('responses', 'Responses'), ('participants', 'Participants')],
        default='responses'
    )
    submit = SubmitField('Download')
    hidden = HiddenField("Download")
