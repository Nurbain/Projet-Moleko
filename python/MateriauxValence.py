def matvalence():
	bpy.ops.object.select_grouped(type='TYPE')
	carb = couleurcarb()
	azote = couleurazote()
	oxy = couleuroxy()
	chlore = couleurchlore()
	fluor = couleurfluor()
	soufre = couleursoufre()
	listec = [carb]
	listea = [azote]
	listeo = [oxy]
	listechl = [chlore]
	listef = [fluor]
	listes = [soufre]
	liste = []
	for objet in bpy.context.selected_objects :
			bpy.context.scene.objects.active = objet
			if 'Carb' in objet.name:
				bpy.context.scene.objects.active = objet
				listec.append(bpy.context.active_object.children)
			if 'Azo' in objet.name :
				bpy.context.scene.objects.active = objet
				listea.append(bpy.context.active_object.children)
			if 'Oxy' in objet.name :
				bpy.context.scene.objects.active = objet
				listeo.append(bpy.context.active_object.children)
			if 'Chlo' in objet.name :
				bpy.context.scene.objects.active = objet
				listechl.append(bpy.context.active_object.children)
			if 'Flu' in objet.name :
				bpy.context.scene.objects.active = objet
				listef.append(bpy.context.active_object.children)
			if 'Souf' in objet.name :
				bpy.context.scene.objects.active = objet
				listes.append(bpy.context.active_object.children)
	liste.append(listec)
	liste.append(listea)
	liste.append(listeo)
	liste.append(listechl)
	liste.append(listef)
	liste.append(listes)
	return liste