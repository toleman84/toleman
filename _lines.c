#include "main.h"

/**
 *
 *
 */

char *lsh_read_line(void)
{
	char *line = NULL, *buffer = NULL, **tokens, *token;
	ssize_t bufsize;
	size_t n = 0;
	int position = 0, c, i;
	const char *delim = " \t\r\n\a";

	bufsize = getline(&line, &n, stdin);
	{
		if (bufsize == -1) /* we received an EOF */
			exit(EXIT_SUCCESS);
		else
			perror("ESHELL: getline\n"), exit(EXIT_FAILURE);
	}
	buffer = malloc(sizeof(char) * bufsize);

	if (!buffer)
	{
		free(buffer);
		fprintf(stderr, "Eshell: allocation error\n"), exit(EXIT_FAILURE);;
	}
	while (1)
	{
		c = getchar();
		if (c == EOF)
			exit(EXIT_SUCCESS);
		else if (c == '\n')
		{
			buffer[position] = '\0';
			return (buffer);
		}
		else
			buffer[position] = c;
		position++;
	}
	/*return (0);*/
	token = strtok(line, delim);
	while (token != NULL)
	{
		tokens[position] = token;
		position++;
		token = strtok(NULL, delim);
	position++;
	}
	tokens = malloc(position * sizeof(char *));
	if (!tokens)
	{
		fprintf(stderr, "Eshell: allocation error\n");
		exit(EXIT_FAILURE);
	}
	token = strtok(buffer, delim);
	for (i = 0; token != NULL; i++)
	{
		tokens[i] = malloc(sizeof(char) * _strlen(token));
		_strcpy(tokens[i], token);
		token = strtok(NULL, delim);
	}
	tokens[i] = NULL;
/*	return (tokens);*/
}

