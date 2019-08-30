{ pkgs ? import <nixpkgs> {}, devBuild ? true }:

let  
  python-re3 = pkgs.python37.withPackages (ps: with ps; [
    #opencv3
    #tensorflow
    tensorflowWithCuda
    numpy
  ]);
  opencv3-re3 = pkgs.python37.pkgs.opencv3.override { enableGtk3 = true; enableFfmpeg = true; };

in
  pkgs.mkShell {
   name = "myRe3-shell"; 
   buildInputs = [ 
      python-re3
      opencv3-re3
    ];
  }

