import mysql.connector


def allotted_for():

    # Connect to the MySQL database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="MazeRunner12",
        database="elective"
    )

    # Create a cursor
    cursor = connection.cursor(dictionary=True)  # Use dictionary cursor for named fields
    truncate_query = "truncate table allotted_for;"
            
    cursor.execute(truncate_query)

    classrooms=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
    seminar=[22,23,24,2,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
    completed1=[]
    completed2=[]

    subjects=["DA","ARVR","HCI","Cryptography","AA","IOT"]

    for subject in subjects:
        # Call the stored procedure
        params = (subject,)

        cursor.callproc("GetElectiveTeach", params)


        # Fetch the results
        teachers = {}
        teachers_student={}
        for result in cursor.stored_results():
            for row in result:
                row=dict(row)
                teachers[str(row["faculty_id"])]=0
                teachers_student[str(row["faculty_id"])]=[]

                
        prams=(subject,)
        courseid=""
        cursor.callproc('GetCourseID',prams)
        for result in cursor.stored_results():
            for row in result:
                row=dict(row)
                courseid=row['course_id']

        eid=""
        cursor.callproc('GetElectiveID',prams)
        for result in cursor.stored_results():
            for row in result:
                row=dict(row)
                eid=row['elective_id']


        # Call the stored procedure
        params = (subject,)
        cursor.callproc("GetElectiveDeets", params)


        # Fetch the results
        students = []
        for result in cursor.stored_results():
            for row in result:
                students.append(dict(row))



        extra=[]
        for i in students:
            check=0
            if teachers[i['f1']]<60 and check==0:
                check=1
                teachers[i['f1']]+=1
                teachers_student[i['f1']].append(i["srn"])
                if teachers[i['f1']]==60 and teachers[i['f1']] not in completed1:
                    completed1.append(i['f1'])
            elif (i['f2'] is not None) and (teachers[i['f2']]<60) and check==0:
                check=1
                teachers[i['f2']]+=1
                teachers_student[i['f2']].append(i["srn"])
                if teachers[i['f2']]==60 and teachers[i['f2']] not in completed1:
                    completed1.append(i['f2'])
            elif (i['f3'] is not None) and (teachers[i['f3']]<60) and (check==0):
                check=1
                teachers[i['f3']]+=1
                teachers_student[i['f3']].append(i["srn"])
                if teachers[i['f3']]==60 and teachers[i['f3']] not in completed1:
                    completed1.append(i['f3'])
            elif (i['f4'] is not None) and (teachers[i['f4']]<60) and (check==0):
                check=1
                teachers[i['f4']]+=1
                teachers_student[i['f4']].append(i["srn"])
                if teachers[i['f4']]==60 and teachers[i['f4']] not in completed1:
                    completed1.append(i['f4'])
            else:
                extra.append(i["srn"])

        while len(extra)>60:
            fid=completed1.pop()
            teachers_student[fid].extend(extra[-60:])
            extra=extra[:-60]
            teachers[fid]+=60

        if len(extra)>0:
            fid=completed1.pop()
            teachers_student[fid].extend(extra)
            teachers[fid]+=len(extra)





        for i in teachers.keys():
            
            if teachers[i]<=60:
                room=classrooms.pop()
                insert_query = "INSERT INTO allotted_for (Elective_ID, Course_id, Class_id,Faculty_id, SRN) VALUES (%s, %s, %s,%s,%s)"
                value_1=eid
                value_2=courseid
                value_3=room
                value_4=i
                for j in teachers_student[i]:
                    value_5=j
                    cursor.execute(insert_query, (value_1, value_2, value_3,value_4,value_5))
                    connection.commit()
            elif teachers[i]>60:
                room=seminar.pop()
                insert_query = "INSERT INTO allotted_for (Elective_ID, Course_id, Class_id,Faculty_id, SRN) VALUES (%s, %s, %s,%s,%s)"
                value_1=eid
                value_2=courseid
                value_3=room
                value_4=i
                for j in teachers_student[i]:
                    value_5=j
                    cursor.execute(insert_query, (value_1, value_2, value_3,value_4,value_5))
                    connection.commit()            

    print(teachers_student)
    subjects=["BD","GTA","CNS"]
    for subject in subjects:
        # Call the stored procedure
        params = (subject,)

        cursor.callproc("GetElectiveTeach", params)


        # Fetch the results
        teachers = {}
        teachers_student={}
        for result in cursor.stored_results():
            for row in result:
                row=dict(row)
                teachers[str(row["faculty_id"])]=0
                teachers_student[str(row["faculty_id"])]=[]

                
        prams=(subject,)
        courseid=""
        cursor.callproc('GetCourseID',prams)
        for result in cursor.stored_results():
            for row in result:
                row=dict(row)
                courseid=row['course_id']

        eid=""
        cursor.callproc('GetElectiveID',prams)
        for result in cursor.stored_results():
            for row in result:
                row=dict(row)
                eid=row['elective_id']


        # Call the stored procedure
        params = (subject,)
        cursor.callproc("GetElectiveDeets", params)


        # Fetch the results
        students = []
        for result in cursor.stored_results():
            for row in result:
                students.append(dict(row))



        extra=[]
        for i in students:
            check=0
            if teachers[i['f1']]<60 and check==0:
                check=1
                teachers[i['f1']]+=1
                teachers_student[i['f1']].append(i["srn"])
                if teachers[i['f1']]==60 and teachers[i['f1']] not in completed2:
                    completed1.append(i['f1'])
            elif (i['f2'] is not None) and (teachers[i['f2']]<60) and check==0:
                check=1
                teachers[i['f2']]+=1
                teachers_student[i['f2']].append(i["srn"])
                if teachers[i['f2']]==60 and teachers[i['f2']] not in completed2:
                    completed1.append(i['f2'])
            elif (i['f3'] is not None) and (teachers[i['f3']]<60) and (check==0):
                check=1
                teachers[i['f3']]+=1
                teachers_student[i['f3']].append(i["srn"])
                if teachers[i['f3']]==60 and teachers[i['f3']] not in completed2:
                    completed1.append(i['f3'])
            elif (i['f4'] is not None) and (teachers[i['f4']]<60) and (check==0):
                check=1
                teachers[i['f4']]+=1
                teachers_student[i['f4']].append(i["srn"])
                if teachers[i['f4']]==60 and teachers[i['f4']] not in completed2:
                    completed1.append(i['f4'])
            else:
                extra.append(i["srn"])

        while len(extra)>60:
            fid=completed1.pop()
            teachers_student[fid].extend(extra[-60:])
            extra=extra[:-60]
            teachers[fid]+=60

        if len(extra)>0:
            fid=completed1.pop()
            teachers_student[fid].extend(extra)
            teachers[fid]+=len(extra)





        for i in teachers.keys():
            
            if teachers[i]<=60:
                room=classrooms.pop()
                insert_query = "INSERT INTO allotted_for (Elective_ID, Course_id, Class_id,Faculty_id, SRN) VALUES (%s, %s, %s,%s,%s)"
                value_1=eid
                value_2=courseid
                value_3=room
                value_4=i
                for j in teachers_student[i]:
                    value_5=j
                    cursor.execute(insert_query, (value_1, value_2, value_3,value_4,value_5))
                    connection.commit()
            elif teachers[i]>60:
                room=seminar.pop()
                insert_query = "INSERT INTO allotted_for (Elective_ID, Course_id, Class_id,Faculty_id, SRN) VALUES (%s, %s, %s,%s,%s)"
                value_1=eid
                value_2=courseid
                value_3=room
                value_4=i
                for j in teachers_student[i]:
                    value_5=j
                    cursor.execute(insert_query, (value_1, value_2, value_3,value_4,value_5))
                    connection.commit()            



    # Close the cursor and the connection
    cursor.close()
    connection.close()

allotted_for()