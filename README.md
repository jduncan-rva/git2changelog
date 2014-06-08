git2changelog
=============

# Purpose
git2changelog analyzes git repositories to generate formatted changelogs
# Usage
```bash
git2changelog -r REPO -b BEGIN_TAG [-e END_TAG -s SEARCH_STRING]
```
# Options
* -b, --begin_tag=BEGIN_TAG
    the git tag to begin the changelog generation with. this is required since you shouldn't be creating an RPM (and thus a spec file) without a tagged release

* -e, --end_tag=END_TAG
    the git tag to stop the changelog generation with. if none is given it gives all entries up through HEAD, and notes that HEAD commits that haven't been tagged are 'Unreleased'

* -r, --repo=REPO
    the git repository to analyze. this can be a relative or fully-qualified filesystem path, but it must be accessible.

* -s, --search=SEARCH_TERM
    an optional search term used to limit commits that are output into the changelog. a common use would be limit the changelog to commits that fixed a bugzilla or github issue or similar
#Mailing Lists
None Yet
