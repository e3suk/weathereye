"""Console script for weathereye."""
import sys
import click

import weathereye.execute_playbooks as ex


@click.group()
def main(args=None):
    """weathereye command-line interface"""
    return 0


# WeatherEye install command group
@main.group()
def install():
    """WeatherEye install command"""
    pass


# command to install surface cdms
@install.command()
def surface():
    # Confirm SURFACE CDMS install with user
    if not click.confirm(click.style("This will install SURFACE CDMS and additional required dependencies. Proceed?", fg='yellow', bold=True)):
        return

    # begin surface cdms installation
    click.echo("Installing SURFACE CDMS...")

    # install SURFACE
    if not ex.run_surface_playbook():
        return


# command to install surface on a romote machine
@install.command()
def surface_remote():
    # Confirm remote SURFACE CDMS install with user
    if not click.confirm(click.style("This will install SURFACE CDMS and additional required dependencies on remote systems. Proceed?", fg='yellow', bold=True)):
        return
    
    # begin surface cdms installation
    click.echo("Installing SURFACE CDMS...")

    # install SURFACE
    if not ex.remote_run_surface_playbook():
        return
    

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
