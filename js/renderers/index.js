let scene, camera, renderer;

function render_3d_model(model_name) {

    container = document.getElementById(model_name);
    // document.body.appendChild( container );

    renderer = new THREE.WebGLRenderer({antialias:true});

    scene = new THREE.Scene();
    scene.background = new THREE.Color(0xdddddd);

    RATIO = 0.8

    camera = new THREE.PerspectiveCamera(40, 1/1, 1, 5000);
    
    window.addEventListener( 'resize', onWindowResize, true );
    
    // renderer.setSize(window.innerWidth * RATIO, window.innerWidth * RATIO);

    function onWindowResize(){
        camera.aspect = 1/1;
        camera.updateProjectionMatrix();
        
        w = window.innerWidth * RATIO
        if (w > 800) w = 800
            
        renderer.setSize( w , w );
    }

    onWindowResize()

    camera.rotation.y = 0/180*Math.PI;
    camera.position.x = 0;
    camera.position.y = 0;
    camera.position.z = 300;

    controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.update();
    // controls.addEventListener('change', renderer => {console.log(controls.object.position);});
    // controls.addEventListener('change', renderer);

    // controls.addEventListener( "change", event => {console.log( controls.object.position );});

    hlight = new THREE.AmbientLight (0x404040);
    scene.add(hlight);

    // directionalLight = new THREE.DirectionalLight(0xffffff,100);
    // directionalLight.position.set(0,1,0);
    // directionalLight.castShadow = true;
    // scene.add(directionalLight);

    light = new THREE.PointLight(0x404040);
    light.position.set(100,300,500);
    scene.add(light);
    // light2 = new THREE.PointLight(0xc4c4c4,10);
    // light2.position.set(500,100,0);
    // scene.add(light2);
    // light3 = new THREE.PointLight(0xc4c4c4,10);
    // light3.position.set(0,100,-500);
    // scene.add(light3);
    // light4 = new THREE.PointLight(0xc4c4c4,10);
    // light4.position.set(-500,300,500);
    // scene.add(light4);


    // renderer.setSize(width, height);
    container.appendChild( renderer.domElement );

    let loader = new THREE.GLTFLoader();
    
    loader.load(`models/${model_name}.glb`, function(gltf){
        model = gltf.scene.children[0];
        model.position.set(0, 0, 0)
        // model.scale.set(0.5,0.5,0.5);
        scene.add(gltf.scene);
        animate();
    });
}

function animate() {
    // model.rotation.z += 0.001;

    renderer.render(scene, camera);
    requestAnimationFrame(animate);
}
// init(model_name);