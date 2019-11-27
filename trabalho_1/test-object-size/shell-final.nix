{ pkgs ? import <nixpkgs> {}, devBuild ? true }:

let  
  python-AI = pkgs.python37.withPackages (ps: with ps; [
    scipy
    imutils
    numpy
  ]);
  opencv3-AI = pkgs.python37.pkgs.opencv3.override { enableGtk3 = true; enableFfmpeg = true; };

in
  pkgs.mkShell {
   name = "AI-shell"; 
   buildInputs = [ 
      opencv3-AI
      python-AI
    ];
  }

