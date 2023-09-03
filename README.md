## Native Khmer Word to Phonemic

This repo shows how to use [automatic-phonemic-and-phonetic-transcription](https://gitlab.com/mkrlab/automatic-phonemic-and-phonetic-transcription) with `pynini`

Install pynini

```shell
conda install -c conda-forge pynini
```

Run

```shell
python khmer_rewriter.py
```

### Compiling with Thrax

 ```shell
# Install on macOS
brew install thrax

# Compile .grm file to get .far
./compile.sh
```
 
### References

- [automatic-phonemic-and-phonetic-transcription](https://gitlab.com/mkrlab/automatic-phonemic-and-phonetic-transcription) by [@MakaraSok](https://github.com/MakaraSok)
