
# Git:
- Getting started with Git: See [Git Book](https://git-scm.com/book/en/v2) (chapters 1, 2, 3, 6)
- GitHub flow: See [Introduction](https://guides.github.com/introduction/flow/) and [Fork a Repo](https://help.github.com/articles/fork-a-repo/)
- GitHub Markdown: See [Markdown](https://guides.github.com/features/mastering-markdown/)

# Git Software:
- GUI Based: [SourceTree](https://www.sourcetreeapp.com/)
- IDE Based: [VS Code](https://code.visualstudio.com/) + `GitLens`, `Git History` and `GitHub` extensions
- CLI Based: [Git for Windows](https://git-scm.com/download/win) + [Posh Git](https://github.com/dahlbyk/posh-git)

# Git Hooks:
- Strip Notebook metadata on commit: [NbStripout](https://github.com/kynan/nbstripout)

# Creating Releases:
- [Draft a new release](https://github.com/mpr213/lecture-notes/releases)
- Tag version: Follows the pattern `YYYYrevX` (Eg. `2018rev1`)
- Description: A list of merged pull requests with their short summary

# CI (Continuous Integration) + Binder Hosting
- CI done through Travis. Runs on every commit pushed to repo. Used to do spellchecking. See `.travis.yml` and `tasks.py` files.
- CI Process overview:
    - NbConvert: converts notebooks to `.rst` files
    - Sphinx: spellcheck* and url link* checking on `.rst` files
    - *Currently issues are only reported as warnings and not errors so CI always passes regardless.
- Binder: Pretty much sorts itself out. Uses the `postBuild` file to install `nbtutor`