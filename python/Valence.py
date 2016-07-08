def changementvalence(liste):
#sélectionne tout
	carb = couleurcarb()
	azote = couleurazote()
	oxy = couleuroxy()
	chlore = couleurchlore()
	fluor = couleurfluor()
	soufre = couleursoufre()
	bpy.ops.object.select_grouped(type='TYPE')
#liste modele
	listev = []
	listem = []
#ajoute dans la liste les objets modele
	for objet in bpy.context.selected_objects :
		bpy.context.scene.objects.active = objet
#on vérifie si le nom de l'objet contient Hydro , pour vérifier que c'est un hydrogène 
		if 'Valence' in objet.name:
			bpy.context.scene.objects.active = objet
			listev.append(bpy.context.active_object)
		elif 'Model' in objet.name:
			bpy.context.scene.objects.active = objet
			model = bpy.context.active_object
#création des nbr objets
	bpy.ops.object.select_all(action='DESELECT')
	bpy.context.scene.objects.active = model
	model.select=True
	for k in range(0,len(listev)):
		bpy.ops.object.duplicate_move()
		obj=bpy.context.active_object
		listem.append(obj)
#valeur absolue du scaling
		x=listev[k].scale.x
		y=listev[k].scale.y
		z=listev[k].scale.z
#modification scalingobj.
		obj.scale = [x,z,y]
#modification location
		obj.location = [listev[k].location.x,listev[k].location.y,listev[k].location.z]
#modification rotation, le 1.5708 rad correspond a 90° 
		obj.rotation_euler = [listev[k].rotation_euler.x+1.5708,listev[k].rotation_euler.y,listev[k].rotation_euler.z]
#smooth de l'objet
		bpy.ops.object.shade_smooth()
		r = recherche(liste,listev[k].name)
		print (r)
		if (r in "Carb") :
			setcouleur(bpy.context.object,carb)
		elif (r in "Azote") :
			setcouleur(bpy.context.object,azote)
		elif (r in "Oxy") :
			setcouleur(bpy.context.object,oxy)
		elif (r in "Chlore") :
			setcouleur(bpy.context.object,chlore)
		elif (r in "Fluor") :
			setcouleur(bpy.context.object,fluor)
		elif (r in "Soufre") :
			setcouleur(bpy.context.object,soufre)
#couleur de l'objet
#supression des modèles 
	for l in range(0,len(listem)) :
		bpy.ops.object.select_all(action='DESELECT')
		listem[l].select=True
		bpy.context.scene.objects.active = listem[l]
		scaling()
	bpy.ops.object.select_all(action='DESELECT')
	for n in range(0,len(listev)):
		listev[n].select = True
		bpy.ops.object.delete(use_global=False)
