# Local Setup

To set up the repo for local development, follow the steps:

1. Clone the repo
2. Create a virtual environment (my python version is 3.9, versions around that should be fine?)
3. Once you have the venv created, run `source venv/bin/activate` to activate the venv
4. Run `pip install -r requirements.txt` to install dependencies, use pip3 if needed (should not be needed if you have
   venv activated)
5. Start coding :)

# Structure

Code should live in the `src` folder and create subdirectories when necessary (but this seems to be a suboptimal
structure?).

I was not able to figure out how to properly setup `__init__.py` files in subdirectories (or if that is needed at all),
so if you can figure it out, feel free to restructure the project.

# Build and deployment

Use the build script `build.sh` to create a `dist.zip` that can be uploaded onto AWS Lambda. I am also considering
adding workflow to auto deploy (WIP). 