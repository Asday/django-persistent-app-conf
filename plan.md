# User

* Anything calls a function on the app config with a config key set and gets a boolean - whether the config key set is configured;
* View marks itself as dependent on a config set, middleware reroutes the request to a specified view;
* App marks itself as dependent on a config set, middleware reroutes the request to a specified view;
* App config can define config model, (automatically determined otherwise).

# Library

* Custom field that tracks whether it's been set (but how);
  * Config fields start unconfigured, transition to configured once modified, and never change to unconfigured again (allowing for indefinite caching of configured status).
* Middleware that inspects the view/app for config requirements;
* Admin.

# Maybe

* Checks to make sure config model classes referred to are defined?  Easy at runtime, possibly hard at "compile" time, (startup).

# Future

* Sites framework integration if I end up caring enough.
