//Lumière 
	
	var light1 = new THREE.PointLight(0xffffff, 0.5);
    light1.position.set(-200,200,100);
    scene.add(light1);


    var light2 = new THREE.PointLight(0xffffff, 0.5);
    light2.position.set(200,-200,100);
    scene.add(light2);


	var light3 = new THREE.PointLight(0xFFFFFF, 0.5);
    light3.position.set(-200,200,100);
    scene.add(light3);


	var light4 = new THREE.PointLight(0xFFFFFF, 0.5);
    light4.position.set(-200,-200,100);
    scene.add(light3);


	
	var light5 = new THREE.PointLight(0xffffff, 0.5);
      light1.position.set(-200,200,-100);
      scene.add(light5);


    var light6 = new THREE.PointLight(0xffffff, 0.5);
    light6.position.set(200,-200,-100);
    scene.add(light6);



	var light7 = new THREE.PointLight(0xFFFFFF, 0.5);
    light7.position.set(-200,200,-100);
    scene.add(light7);


	var light8 = new THREE.PointLight(0xFFFFFF, 0.5);
    light8.position.set(-200,-200,-100);
    scene.add(light8);

	
	var light9 = new THREE.PointLight(0xffffff, 0.5);
    light1.position.set(200,0,0);
    scene.add(light1);


    var light10 = new THREE.PointLight(0xffffff, 0.5);
    light10.position.set(-200,0,0);
    scene.add(light2);
	
	var light11 = new THREE.PointLight(0xFFFFFF, 0.5);
    light11.position.set(0,200,0);
    scene.add(light11);

	var light12 = new THREE.PointLight(0xFFFFFF, 0.5);
    light12.position.set(0,-200,0);
    scene.add(light12);
	
	var light13 = new THREE.PointLight(0xFFFFFF, 0.5);
    light13.position.set(0,0,200);
    scene.add(light13);
	
	var light14 = new THREE.PointLight(0xFFFFFF, 0.5);
    light14.position.set(0,0,-200);
    scene.add(light14);