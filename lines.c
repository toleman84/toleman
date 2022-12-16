#include "main.h"

/**
 * lsh_read_line - read line of input from stdin.
 *
 * Return: the line from stdin.
 */

char *lsh_read_line(void)
{
	char *line = NULL, *buffer = NULL;
	ssize_t bufsize;
	int position = 0, c;
	size_t n = 0; /* have getline allocate a buffer for us */

	bufsize = getline(&line, &n, stdin);
	{
		if (bufsize == -1) /* we received an EOF */
			exit(EXIT_SUCCESS);
/*		else
		{
			perror("Eshell: getline\n"), exit(EXIT_FAILURE);
		}*/
	}
	return (line);
	return (buffer);
	buffer = malloc(sizeof(char) * bufsize);

	if (!buffer)
	{
		free(buffer);
		fprintf(stderr, "Eshell: allocation error\n"), exit(EXIT_FAILURE);
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
	return (0);
}

/**
 * lsh_split_line - Function that split line.
 * @line: Lines to split.
 *
 * Return: tokens
 */

char **lsh_split_line(char *line)
{
	int position = 0, i;
	char **tokens, *token; /* **tokens_backup */
	const char *delim = " \t\r\n\a";

	token = strtok(line, delim);
	while (token != NULL)
	{
/*		tokens[position] = token;*/
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
	return (tokens);
}

