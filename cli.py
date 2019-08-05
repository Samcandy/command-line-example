import click, os


@click.group()
def cli1():
    '''    My Command Line    '''
    pass

@cli1.command()
@click.option('-d', '--deployment_name', help='', required=False)
@click.option('-b', '--bridge_name', help='', required=False)
@click.option('-i', '--interface_name', help='', required=False)
@click.option('-e', '--env', help='', required=False)
def show(deployment_name, bridge_name, interface_name, env):
    '''    Show something    '''
    if deployment_name:
        click.echo(deployment_name)
    if bridge_name:
        click.echo(bridge_name)
    if interface_name:
        click.echo(interface_name)
    if env:
        click.echo('POD_NAME: {}'.format(os.environ['POD_NAME']))
        click.echo('POD_NAMESPACES: {}'.format(os.environ['POD_NAMESPACES']))
        click.echo('POD_UUID: {}'.format(os.environ['POD_UUID']))

@cli1.command()
@click.option('-n', '--name', help='', required=False)
def cidr(name):
    '''    Show cidr   '''
    click.echo('cidr')

cli = click.CommandCollection(sources=[cli1])
if __name__ == '__main__':
    cli()

