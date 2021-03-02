Installation
------------

To make a script accessible from command line without specifying its
path, create a symbolic link to it in a directory that is part of your
`$PATH` env variable.

```bash
ln -s script_example.sh $link_path
```

Alternatively, you can add the following line to your `.bashrc` (or equivalent)
```bash
export SLURM_TB=<path to this project directory>
```

then run scripts using
```bash
$SLURM_TB/script_example.sh
```