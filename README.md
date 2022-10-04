# Dummy data generator (dtg) 🤡 🎲

## Usage

```
usage: dtg [-v | --version] [-h | --help] <command> [args]
```

(dtg) A command line utility to generate dummy data. dtg has 4 commands to use, which are:

- parse: Generate dummy data based on json file template
```
dtg parse model.json [--intelligentia]
```

---

- create: Initializes the creation of a dummy data model
```
dtg create <modelname> [--path=<path>]
```

---

- add: Adds (a) field(s) to the dummy data model
```
dtg add [--field=<field:type>] [[--parse <file>] --force]
```

---

- reset: Redefines a dummy data model
```
dtg reset modelname
```

### NOTE: More commands will be idealized and later added to the project. So, currently this is just an idealization of what the project will become. 🚧⛔️💻
