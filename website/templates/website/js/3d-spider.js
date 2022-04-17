"use strict";

import * as THREE from 'https://unpkg.com/three@0.126.1/build/three.module.js';


const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(
    75,
    window.innerWidth / window.innerHeight,
    0.1,
    1000
);

const renderer = new THREE.WebGLRenderer();

const loader = new THREE.ObjectLoader();
loader.load(
    'mtlModels/Only_Spider_with_Animations_Export.obj',
    function(object) {
        scene.add(object);
    }
);





//
// //
// // console.log("11");
//
//
// import * as THREE from 'https://unpkg.com/three@0.126.1/build/three.module.js';
// import * as AA from "https://threejs.org/examples/jsm/controls/OrbitControls.js";
//
// var scene = new THREE.Scene();
// var camera = new THREE.PerspectiveCamera(
//     75,
//     window.innerWidth/window.innerHeight,
//     0.1,
//     1000
// );
//
// var renderer = new THREE.WebGLRenderer();
//
// renderer.setSize(window.innerWidth, window.innerHeight);
// document.body.appendChild(renderer.domElement);
//
// var geometry = new THREE.BoxGeometry(1,1,1);
// var material = new THREE.MeshBasicMaterial(
//     {
//         color: 0x00ff00
//     }
// );
//
// camera.position.z = 200;
//
// var controls = new AA.OrbitControls(camera, renderer.domElement);
// controls.enableDamping = true;
// controls.campingFactor = 0.25;
// controls.enableZoom = true;
//
// var keyLight = new THREE.DirectionalLight(
//     new THREE.Color('hsl(30,100%,75%)'), 1.0
// );
// keyLight.position.set(-100, 0, 100);
//
// var fillLight = new THREE.DirectionalLight(
//     new THREE.Color('hsl(240,100%,75%)'), 0.75
// );
// fillLight.position.set(100,0,100);
//
// var backLight = new THREE.DirectionalLight(0xffffff, 1.0);
// backLight.position.set(100,0,-100).normalize();
//
// scene.add(keyLight);
// scene.add(fillLight);
// scene.add(backLight);
//
// var mtlLoader = new THREE.MTLLoader();
//
// var objLoader = new THREE.OBJLoader();
//     objLoader.setPath('mtlModels/');
//     objLoader.load('Only_Spider_with_Animations_Export.obj', function(object){
//         object.position.y -=60;
//         scene.add(object);
//     });
//
// // mtlLoader.setTexturePath('mtlModels/');
// // mtlLoader.setPath('mtlModels/');
// // mtlLoader.load('Only_Spider_with_Animations_Export.mtl', function(object) {
// //     material.preload();
// //
// //     var objLoader = new THREE.OBJLoader();
// //     objLoader.setPath('mtlModels/');
// //     objLoader.load('Only_Spider_with_Animations_Export.obj', function(object){
// //         object.position.y -=60;
// //         scene.add(object);
// //     })
// // })
// // );
//
// var animate = function() {
//     requestAnimationFrame(animate);
//     controls.update();
//     renderer.render(scene, camera);
// };
//
// animate();
//
//
//
//
//
