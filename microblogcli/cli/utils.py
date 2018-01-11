import click


__all__ = ['format_with_suggestion']


def format_with_suggestion(message, suggestion):
	suggestion = click.style(suggestion, bg='white', fg='blue')
	return f'{message}\n{suggestion}'
