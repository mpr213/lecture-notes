import os
import glob
import re
import sys

from invoke import task


def run(ctx, *args, **kwargs):
    if 'pty' not in kwargs:
        kwargs['pty'] = True
    if 'echo' not in kwargs:
        kwargs['echo'] = True
    return ctx.run(*args, **kwargs)


@task
def execute_notebooks(ctx):
    """Execute notebooks"""
    root = os.path.abspath(os.getcwd())
    print("Executing notebooks...")

    cwd = os.getcwd()
    os.chdir(root)

    for filename in sorted(glob.glob('*.ipynb')):
        if 'demo' in filename.lower():
            continue

        run(ctx, ' '.join([
            sys.executable, '-m', 'jupyter', 'nbconvert',
            '--inplace',
            '--execute',
            '--ExecutePreprocessor.allow_errors=True',
            filename
        ]))

    os.chdir(cwd)


@task
def convert_notebooks(ctx):
    """Convert notebooks to rst and html"""
    root = os.path.abspath(os.getcwd())
    print("Converting notebooks...")

    cwd = os.getcwd()
    os.chdir(root)

    for filename in sorted(glob.glob('*.ipynb')):
        run(ctx, ' '.join([
            sys.executable, '-m', 'jupyter', 'nbconvert',
            '--to', 'rst',
            '--FilesWriter.build_directory=sphinx/source',
            filename
        ]))

    # hack to convert links to ipynb files to html
    for filename in sorted(glob.glob('sphinx/source/*.rst')):
        with open(filename, 'r') as fh:
            source = fh.read()
        source = re.sub(r"<([^><]*)\.ipynb>", r"<\1.html>", source)
        with open(filename, 'w') as fh:
            fh.write(source)

    os.chdir(cwd)


@task
def clean_sphinx(ctx):
    print("Removing .rst files in 'sphinx'...")
    run(ctx, 'git clean -fdx sphinx')


@task
def clear_notebooks_output(ctx):
    """Clear output from notebooks cells"""
    root = os.path.abspath(os.getcwd())
    print("Clearing output from notebook cells...")

    cwd = os.getcwd()
    os.chdir(root)

    for filename in sorted(glob.glob('*.ipynb')):
        run(ctx, ' '.join([
            sys.executable, '-m', 'jupyter', 'nbconvert',
            '--inplace',
            '--to', 'ipynb',
            '--ClearOutputPreprocessor.enabled=True',
            filename
        ]))

    os.chdir(cwd)


@task
def check_notebooks(ctx, skip_execute=False):
    print("Running setup...")
    clean_sphinx(ctx)
    if not skip_execute:
        execute_notebooks(ctx)
    convert_notebooks(ctx)
    print("Checking notebooks...")
    run(ctx, 'make -C sphinx spelling')
    run(ctx, 'make -C sphinx linkcheck')
