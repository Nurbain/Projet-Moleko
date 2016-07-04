def changementgeneral() :
#sélectionne tout
	bpy.ops.object.select_grouped(type='TYPE')
#création couleur 
	carb = couleurcarb()
	azote = couleurazote()
	oxy = couleuroxy()
	chlore = couleurchlore()
	fluor = couleurfluor()
	soufre = couleursoufre()
#liste modele
	listec = [carb]
	listea = [azote]
	listeo = [oxy]
	listechl = [chlore]
	listef = [fluor]
	listes = [soufre]
	liste = []
#ajoute dans les liste les objets modele correspondant
	for objet in bpy.context.selected_objects :
		bpy.context.scene.objects.active = objet
		if 'Carb' in objet.name:
			bpy.context.scene.objects.active = objet
			listec.append(bpy.context.active_object)
		if 'Azo' in objet.name :
			bpy.context.scene.objects.active = objet
			listea.append(bpy.context.active_object)
		if 'Oxy' in objet.name :
			bpy.context.scene.objects.active = objet
			listeo.append(bpy.context.active_object)
		if 'Chlo' in objet.name :
			bpy.context.scene.objects.active = objet
			listechl.append(bpy.context.active_object)
		if 'Flu' in objet.name :
			bpy.context.scene.objects.active = objet
			listef.append(bpy.context.active_object)
		if 'Souf' in objet.name :
			bpy.context.scene.objects.active = objet
			listes.append(bpy.context.active_object)
		else : print("L'objet :"+objet.name+" n'a pas pu etre identifié , et donc non modifié")
#création des nbr objets
	liste.append(listec)
	liste.append(listea)
	liste.append(listeo)
	liste.append(listechl)
	liste.append(listef)
	liste.append(listes)
	for i in range(0,len(liste)):
		for j in range(1,len(liste[i])):
			bpy.ops.mesh.primitive_uv_sphere_add()
			obj=bpy.context.active_object
			x=liste[i][j].scale.x
			y=liste[i][j].scale.y
			z=liste[i][j].scale.z
			obj.scale = [x,y,z]
			scaling()
			obj.location = [liste[i][j].location.x,liste[i][j].location.y,liste[i][j].location.z]
			obj.rotation_euler = [liste[i][j].rotation_euler.x,liste[i][j].rotation_euler.y,liste[i][j].rotation_euler.z]
			bpy.ops.object.shade_smooth()
			setcouleur(bpy.context.object,liste[i][0])
			obj.select = False
#supression des modèles 
	for k in range(0,len(liste)):
		for n in range(1, len(liste[k])) :
			liste[k][n].select = True
			bpy.ops.object.delete(use_global=False)		
	