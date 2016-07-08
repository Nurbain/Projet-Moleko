#Nathan Urbain
#Optimisation automatique des molécules

import bpy,bmesh

#Couleur hydrogène et liasion simple 
def couleurhydro() :
	mat = bpy.data.materials.new('Hydro')
	mat.diffuse_color = (1,1,1)
	mat.diffuse_shader = 'LAMBERT' 
	mat.diffuse_intensity = 1.0
	mat.specular_color = (1,1,1)
	mat.specular_shader = 'COOKTORR'
	mat.specular_intensity = 0.032
	mat.ambient = 1
	return mat

#Couleur carbone
def couleurcarb() :
	mat = bpy.data.materials.new('Carbon')
	mat.diffuse_color = (0,0,0)
	mat.diffuse_shader = 'LAMBERT' 
	mat.diffuse_intensity = 1.0
	mat.specular_color = (1,1,1)
	mat.specular_shader = 'COOKTORR'
	mat.specular_intensity = 0.032
	mat.ambient = 1
	return mat

#Couleur azote
def couleurazote() :
	mat = bpy.data.materials.new('Azote')
	mat.diffuse_color = (0,0.144,0.451)
	mat.diffuse_shader = 'LAMBERT' 
	mat.diffuse_intensity = 1.0
	mat.specular_color = (1,1,1)
	mat.specular_shader = 'COOKTORR'
	mat.specular_intensity = 0.032
	mat.ambient = 1
	return mat

#Couleur oxygène
def couleuroxy() :
	mat = bpy.data.materials.new('Oxy')
	mat.diffuse_color = (0.617,0.034,0.010)
	mat.diffuse_shader = 'LAMBERT' 
	mat.diffuse_intensity = 1.0
	mat.specular_color = (1,1,1)
	mat.specular_shader = 'COOKTORR'
	mat.specular_intensity = 0.032
	mat.ambient = 1
	return mat	

#Couleur chlore
def couleurchlore() :
	mat = bpy.data.materials.new('Chlore')
	mat.diffuse_color = (0,0.279,0.037)
	mat.diffuse_shader = 'LAMBERT' 
	mat.diffuse_intensity = 1.0
	mat.specular_color = (1,1,1)
	mat.specular_shader = 'COOKTORR'
	mat.specular_intensity = 0.032
	mat.ambient = 1
	return mat

#Couleur fluor
def couleurfluor() :
	mat = bpy.data.materials.new('Fluor')
	mat.diffuse_color = (0.292,0.006,0.209)
	mat.diffuse_shader = 'LAMBERT' 
	mat.diffuse_intensity = 1.0
	mat.specular_color = (1,1,1)
	mat.specular_shader = 'COOKTORR'
	mat.specular_intensity = 0.032
	mat.ambient = 1
	return mat

#Couleur soufre
def couleursoufre () :
	mat = bpy.data.materials.new('Soufre')
	mat.diffuse_color = (1,0.6,0)
	mat.diffuse_shader = 'LAMBERT' 
	mat.diffuse_intensity = 1.0
	mat.specular_color = (1,1,1)
	mat.specular_shader = 'COOKTORR'
	mat.specular_intensity = 0.032
	mat.ambient = 1
	return mat

#Met la couleur
def setcouleur(obj,mat):
	ob = obj.data
	for k in range(0,len(bpy.context.object.data.materials)):
		bpy.ops.object.material_slot_remove()
	ob.materials.append(mat)

#Change les hydrogènes

def changementhydro():
#sélectionne tout
	bpy.ops.object.select_grouped(type='TYPE')
	mat=couleurhydro()
#sert de conteur pour créer nbr objet
#liste modele
	listem = []
#ajoute dans la liste les objets modele
	for objet in bpy.context.selected_objects :
		bpy.context.scene.objects.active = objet
#on vérifie si le nom de l'objet contient Hydro , pour vérifier que c'est un hydrogène 
		if 'Hydro' in objet.name:
			bpy.context.scene.objects.active = objet
			listem.append(bpy.context.active_object)
#création des nbr objets
	for k in range(0,len(listem)):
		bpy.ops.mesh.primitive_uv_sphere_add()
		obj=bpy.context.active_object
#valeur absolue du scaling
		x=abs(listem[k].scale.x)
		y=abs(listem[k].scale.y)
		z=abs(listem[k].scale.z)
#modification scaling
		obj.scale = [x,y,z]
#modification location
		obj.location = [listem[k].location.x,listem[k].location.y,listem[k].location.z]
#modification rotation
		obj.rotation_euler = [listem[k].rotation_euler.x,listem[k].rotation_euler.y,listem[k].rotation_euler.z]
#smooth de l'objet
		bpy.ops.object.shade_smooth()
#couleur de l'objet
		setcouleur(bpy.context.object,mat)
		obj.select = False
#supression des modèles 
	for n in range(0,len(listem)):
		listem[n].select = True
		bpy.ops.object.delete(use_global=False)

#Change les Lisaions simples	
def changementliaisons():
#sélectionne tout
	bpy.ops.object.select_grouped(type='TYPE')
	mat=couleurhydro()
#sert de conteur pour créer nbr objet
	nbr = 0
#liste modele
	listem = []
#ajoute dans la liste les objets modele
	for objet in bpy.context.selected_objects :
		bpy.context.scene.objects.active = objet
#on vérifie si le nom de l'objet contient Hydro , pour vérifier que c'est un hydrogène 
		if 'Simple' in objet.name:
			nbr=nbr+1
			bpy.context.scene.objects.active = objet
			listem.append(bpy.context.active_object)
#création des nbr objets
	for k in range(0,nbr):
		bpy.context.scene.cursor_location = (0.0, 0.0, 0.0)
		bpy.ops.mesh.primitive_cylinder_add()
		bpy.context.scene.cursor_location = (0,0,1)
#mode edit
		bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
#modification scaling
		obj=bpy.context.active_object
		obj.scale = [listem[k].scale.x,listem[k].scale.y,listem[k].scale.z]
#modification location
		obj.location = [listem[k].location.x,listem[k].location.y,listem[k].location.z]
#modification rotation
		obj.rotation_euler = [listem[k].rotation_euler.x,listem[k].rotation_euler.y,listem[k].rotation_euler.z]
#smooth de l'objet
		bpy.ops.object.shade_smooth()
#couleur de l'objet
		setcouleur(bpy.context.object,mat)
		obj.select = False
#supression des modèles 
	for n in range(0,nbr):
		listem[n].select = True
		bpy.ops.object.delete(use_global=False)

		
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
	
#Fonction effectuant le travail de remise des normals 
def scaling() :
	if bpy.context.active_object.scale.y < 0 :
		bpy.ops.object.transform_apply(location=False , rotation=False , scale=True)
		obj=bpy.context.active_object
		bpy.ops.object.mode_set(mode='EDIT')
		bpy.ops.mesh.select_all(action = 'SELECT')
		bpy.ops.mesh.normals_make_consistent(inside=False)
		bpy.ops.object.mode_set(mode='OBJECT')		


def recherche(liste,valence) :

	r=""
	for k in range(0,len(liste)):
		for l in range(1,len(liste[k])):
			for n in range(0,len(liste[k][l])):
				if (valence==liste[k][l][n].name):
					r=liste[k][0].name
	return r

	
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
			bpy.ops.object.material_slot_remove()
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
		r =recherche(liste,listev[k].name)
		if (r in "Carbon") :
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

	

#Fonction général effectuant le travaille , main 
def optimisation():
	liste=matvalence()
	bpy.ops.object.select_grouped(type='TYPE')
	bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
	changementvalence(liste)
	changementgeneral()
	changementliaisons()
	changementhydro()

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
	
optimisation()